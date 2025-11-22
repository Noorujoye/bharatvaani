import streamlit as st
import os
import pandas as pd
from datetime import datetime
from backend.llm_service import generate_response
from PyPDF2 import PdfReader

# ========= Paths =========
TEXT_CORPUS = "corpus/text/"
IMAGE_CORPUS = "corpus/images/"
DOC_CORPUS = "corpus/documents/"
FEEDBACK_FILE = "feedback/user_feedback.csv"

# ========= Page Config =========
st.set_page_config(
    page_title="BharatVaani – Hindi Cultural AI Assistant",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ========= Sidebar =========
with st.sidebar:
    st.title("🇮🇳 BharatVaani")
    st.markdown(
        """
        **Hindi Cultural AI Assistant**

        - Primary language: **Hindi**
        - UI language: **English**
        - Focus: Indian culture, stories, recipes, festivals, local wisdom  
        - Tech: **Streamlit + Gemini**

        👉 You can:
        - Ask questions in Hindi or English  
        - Share cultural stories, recipes, proverbs  
        - Upload images / PDFs as supporting content  
        """
    )
    st.markdown("---")
    st.markdown("**Data Collection**")
    st.caption(
        "Your text, images and documents are stored locally as cultural corpus "
        "to help build Indic datasets."
    )

# ========= Header / Top Section =========
st.markdown(
    "<h2 style='margin-bottom:0'>🇮🇳 BharatVaani – Hindi Cultural AI Assistant</h2>",
    unsafe_allow_html=True,
)
st.caption("Culture • Tradition • Heritage • Stories • Recipes")

st.markdown(
    """
    **How to use this:**
    - Type your question or share cultural knowledge (preferably in Hindi).  
    - Optionally upload an image or a PDF/document related to your content.  
    - BharatVaani will respond in Hindi, with short and clear answers.
    """
)

st.markdown("---")

# ========= Layout: Two Columns =========
col_left, col_right = st.columns([2.2, 1.3])

with col_left:
    st.subheader("💬 Ask / Share")

    user_query = st.text_area(
        "Type your question or cultural content here (Hindi or English):",
        placeholder="Example: \"मैं होली की एक परंपरा के बारे में बताना चाहता हूँ\"",
        height=120,
    )

    uploaded_image = st.file_uploader(
        "Upload a related image (optional)",
        type=["png", "jpg", "jpeg"],
    )

    uploaded_doc = st.file_uploader(
        "Upload a related document (optional: PDF, TXT, DOCX)",
        type=["pdf", "txt", "docx"],
    )

    st.markdown("")

    send_btn = st.button("Send / भेजें", use_container_width=True)

with col_right:
    st.subheader("📊 Quick Info")
    st.markdown(
        """
        - Responses: **Short, clear, Hindi-first**  
        - Input: Hindi or English (mixed also fine)  
        - Cultural safety: avoids offensive / biased content  
        - Corpus: Saved locally in `corpus/` folders  
        """
    )

    st.markdown("---")
    st.subheader("📁 Stored Data (local only)")
    st.caption("Your contributions are stored as files on the server machine.")

# ========= Helper: Extract text from PDF =========
def extract_pdf_text(file, max_pages=5, max_chars=4000):
    try:
        reader = PdfReader(file)
        text = ""
        for i, page in enumerate(reader.pages[:max_pages]):
            page_text = page.extract_text() or ""
            text += page_text + "\n\n"
        return text[:max_chars]
    except Exception:
        return ""

# ========= Main Logic =========
if send_btn:
    if user_query.strip() == "":
        st.warning("Please type something before sending.")
    else:
        # Build query for model
        final_query = user_query

        # If PDF uploaded, extract its text and append to query for context
        pdf_text = ""
        if uploaded_doc is not None and uploaded_doc.type == "application/pdf":
            pdf_text = extract_pdf_text(uploaded_doc)
            if pdf_text:
                final_query += (
                    "\n\nBelow is the text content of a PDF the user attached. "
                    "Use it as context while answering their question:\n\n"
                    + pdf_text
                )

        with st.spinner("Thinking... / सोच रहा है..."):
            response = generate_response(final_query)

        st.markdown("### 🪔 BharatVaani's Response:")
        st.write(response)

        # ===== Store text corpus =====
        os.makedirs(TEXT_CORPUS, exist_ok=True)
        os.makedirs(IMAGE_CORPUS, exist_ok=True)
        os.makedirs(DOC_CORPUS, exist_ok=True)

        if user_query:
            file_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(os.path.join(TEXT_CORPUS, file_name), "w", encoding="utf-8") as f:
                f.write(user_query)

        # ===== Store image corpus =====
        if uploaded_image is not None:
            img_ext = os.path.splitext(uploaded_image.name)[1] or ".jpg"
            img_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}{img_ext}"
            with open(os.path.join(IMAGE_CORPUS, img_name), "wb") as f:
                f.write(uploaded_image.read())

        # ===== Store document corpus =====
        if uploaded_doc is not None:
            doc_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uploaded_doc.name}"
            with open(os.path.join(DOC_CORPUS, doc_name), "wb") as f:
                f.write(uploaded_doc.read())

        st.success("Your contribution has been stored. Thank you! 🙏")

# ========= Feedback Section =========
st.markdown("---")
st.subheader("⭐ User Feedback")

rating = st.slider("Satisfaction Rating (1 = poor, 5 = excellent)", 1, 5, 4)
feedback_text = st.text_input("Feedback (optional)", placeholder="Write your feedback here...")

if st.button("Submit Feedback", use_container_width=True):
    fb_data = {
        "timestamp": datetime.now(),
        "rating": rating,
        "feedback": feedback_text,
    }
    df = pd.DataFrame([fb_data])

    os.makedirs(os.path.dirname(FEEDBACK_FILE), exist_ok=True)

    if not os.path.exists(FEEDBACK_FILE):
        df.to_csv(FEEDBACK_FILE, index=False)
    else:
        df.to_csv(FEEDBACK_FILE, mode="a", header=False, index=False)

    st.success("Thank you! Your feedback has been recorded. 💬")
