# bharatvaani
🇮🇳 BharatVaani – Hindi Cultural AI Assistant

BharatVaani is an open-source multilingual cultural AI assistant designed to preserve and promote India’s cultural heritage by collecting user-generated stories, recipes, proverbs, festival traditions, and local wisdom in Hindi (primary) + English.

This project was developed as part of the Viswam.ai – Summer of AI Internship 2025, aligned with the goals of Indic language AI, dataset creation, and open-source LLM adoption.

🌍 Core Purpose

✔ Make AI accessible in Indian languages
✔ Collect natural cultural corpus from users
✔ Encourage Indians to contribute to preserving heritage
✔ Support low-bandwidth accessibility

✨ Features
Feature	Status
Hindi + English bilingual conversation	✔
Streamlit-based clean UI	✔
LangChain + Hugging Face open-source LLM	✔
Corpus collection (text, image, document)	✔
User feedback + rating storage	✔
Privacy focused – no third-party data scraping	✔
🧠 Tech Stack
Layer	Technology
Frontend	Streamlit
AI / Backend	LangChain + Hugging Face open-source model
Model (default)	google/gemma-2b-it
Deployment (planned)	Hugging Face Spaces
Corpus Storage	Local structured dataset folders
📂 Project Structure
bharatvaani/
│── app.py
│── backend/
│     ├── llm_service.py
│     ├── prompts.py
│── corpus/
│     ├── text/
│     ├── images/
│     ├── documents/
│── feedback/
│     ├── user_feedback.csv
│── requirements.txt
│── README.md
│── REPORT.md      (to be added)
│── CONTRIBUTING.md
│── CHANGELOG.md
│── LICENSE

🚀 Local Setup
git clone https://github.com/Noorujoye/bharatvaani.git
cd bharatvaani
pip install -r requirements.txt


Create .env file in project root:

HUGGINGFACE_API_KEY=your_token_here


Run app:

streamlit run app.py

🔧 Deployment Roadmap

 Deploy to Hugging Face Spaces

 Collect 10+ user reviews

 Improve responses based on feedback

 Add more Indic languages

🤝 Contributions

This project is open-source and contributions are welcomed.
See CONTRIBUTING.md for guidelines.

📜 License

This project is licensed under the MIT License.

🌟 Acknowledgment

This project is made possible thanks to open-source LLM initiatives, LangChain community, and Viswam.ai’s mission toward Indic AI innovation.
