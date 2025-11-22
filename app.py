import streamlit as st
import os
import pandas as pd
from datetime import datetime
from backend.llm_service import generate_response

# Folder paths
TEXT_CORPUS = "corpus/text/"
IMAGE_CORPUS = "corpus/images/"
DOC_CORPUS = "corpus/documents/"
FEEDBACK_FILE = "feedback/user_feedback.csv"

# Page Config
st.set_page_config(page_title="BharatVaani – Hindi Cultural AI", layout="wide")

# App Title
st.title("🇮🇳 BharatVaani – Hindi Cultural AI Assistant")
st.write("संस्कृति • परंपरा • विरासत • अनुभव • व्यंजन • कहानियाँ\n")

# User Input
user_query = st.text_area("अपना प्रश्न या सांस्कृतिक जानकारी यहाँ साझा करें 👇 (Hindi + English supported)")

# Upload Inputs Section
uploaded_image = st.file_uploader("कोई संबंधित चित्र अपलोड करें (वैकल्पिक)", type=["png", "jpg", "jpeg"])
uploaded_doc = st.file_uploader("कहानी/रेसिपी/उत्सव की जानकारी वाली डॉक्यूमेंट फ़ाइल (वैकल्पिक)", type=["pdf", "txt", "docx"])

# Generate Button
if st.button("Send / भेजें"):
    if user_query.strip() == "":
        st.warning("❕ कृपया कुछ लिखें")
    else:
        with st.spinner("सोच रहा है... / Thinking..."):
            response = generate_response(user_query)
        
        st.markdown("### 🪔 BharatVaani का उत्तर:")
        st.write(response)

        # Store text corpus
        if user_query:
            file_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(os.path.join(TEXT_CORPUS, file_name), "w", encoding="utf-8") as f:
                f.write(user_query)

        # Store image corpus
        if uploaded_image:
            img_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            with open(os.path.join(IMAGE_CORPUS, img_name), "wb") as f:
                f.write(uploaded_image.read())

        # Store document corpus
        if uploaded_doc:
            doc_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uploaded_doc.name}"
            with open(os.path.join(DOC_CORPUS, doc_name), "wb") as f:
                f.write(uploaded_doc.read())

        st.success("🙏 आपका योगदान सुरक्षित कर लिया गया है — धन्यवाद!")

# Feedback Section
st.markdown("---")
st.subheader("⭐ उपयोगकर्ता प्रतिक्रिया / User Feedback")

rating = st.slider("संतुष्टि रेटिंग दें (1 से 5)", min_value=1, max_value=5, value=4)
feedback_text = st.text_input("फीडबैक (वैकल्पिक)")

if st.button("Submit Feedback / फीडबैक भेजें"):
    fb_data = {
        "timestamp": datetime.now(),
        "rating": rating,
        "feedback": feedback_text
    }
    df = pd.DataFrame([fb_data])

    # Store feedback
    if not os.path.exists(FEEDBACK_FILE):
        df.to_csv(FEEDBACK_FILE, index=False)
    else:
        df.to_csv(FEEDBACK_FILE, mode="a", header=False, index=False)

    st.success("💬 धन्यवाद! आपकी प्रतिक्रिया प्राप्त हो गई है।")
