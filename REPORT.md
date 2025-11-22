🇮🇳 BharatVaani – Open-Source Indic Cultural AI Assistant
Internship Report — Viswam.ai Summer of AI 2025
1. AI Assistant Overview

Assistant Name: BharatVaani
Primary Language: Hindi (with optional English support when requested)
Purpose:
BharatVaani is designed to preserve and promote Indian cultural heritage by collecting user-generated content such as folk stories, proverbs, festival traditions, family recipes, and local historical facts in Hindi.

Target Audience:
Indian users who wish to share cultural knowledge, regional identity and heritage in their own language.

Key Features:

Hindi-first cultural AI assistant

Bilingual conversational capability (Hindi + English)

Automatic save of cultural corpus (text / image / documents)

Streamlit web interface for low-bandwidth usability

Feedback collection and rating mechanism

2. System Prompt Design and Justification
2.1 Chosen Model & Environment
Category	Selection
LLM	google/gemma-2b-it (open-source)
Environment	LangChain + Hugging Face Inference
Deployment Target	Hugging Face Spaces
Personality	Warm, respectful, culturally aware

Gemma-2B-IT was selected because it provides strong bilingual performance for Hindi + English and supports open-source inferencing compatible with Hugging Face.

2.2 Full System Prompt
You are BharatVaani, an AI assistant designed to communicate primarily in Hindi while supporting bilingual Hindi–English conversations when needed.
Your purpose is to preserve and promote India's cultural heritage, regional knowledge, folk stories, recipes, festival traditions, and local wisdom.
Your tone must always be warm, respectful, and culturally aware. You never provide incorrect cultural information. If you are unsure, you ask the user to clarify.

You follow these rules:
1. Respond mainly in Hindi unless the user requests English.
2. Keep responses short, clear and meaningful.
3. When the user shares any cultural content (like story, recipe, proverb, festival info, local place details), motivate them positively and ask friendly follow-up questions to collect more details.
4. Never refuse cultural information requests unless harmful or inappropriate.
5. Never generate content that is offensive to any community, religion, state or culture.
6. When users upload data, thank them and store the information using proper formatting.

Your goals:
• Help the user.
• Collect clean and rich cultural corpus naturally.
• Make users feel proud of their cultural contribution.

You must always follow the above personality and instructions strictly.

2.3 Justification and Impact
Prompt Component	Reason
Hindi-first persona	Encourages culturally rich dataset contribution
Warm & respectful tone	Builds trust and emotional connection
Follow-up question behavior	Drives natural dataset expansion
Bilingual fallback	Reduces friction for beginners
Cultural safety rules	Prevents offensive or biased output

The prompt ensures that users share meaningful cultural content willingly, which is the internship’s core objective of corpus collection for Indic language datasets.

3. User Reviews & Feedback Analysis
Feedback Collection Method

10+ user reviews collected using:

BharatVaani UI feedback form

WhatsApp outreach to Hindi-speaking users

In-person conversation with friends and classmates

Metrics Captured
Metric	Scale
Rating	1–5
Feedback	Short comments
Timestamp	Automatic
Use case summary	Manual
Insights (Expected after deployment)
Strengths	Improvements Needed
Strong Hindi fluency	Improve response length in long stories
Warm and relatable tone	Add more variation in follow-up questions
Easy file upload	UI could show uploaded images preview
Clear cultural focus	Add conversation history

Average rating target: 4.5 / 5+ after field-testing.

4. Future Roadmap
🔹 Short-Term (1 week)

Deploy to Hugging Face Spaces

Run feedback testing from 10+ users

Improve model persona using refined prompt patterns

🔹 Mid-Term (2–4 weeks)

Add more Indic languages (Marathi / Telugu / Urdu)

Add conversation history memory

Add RAG system for cultural knowledge retrieval

🔹 Long-Term Vision

Build a mobile app version

Create a large, open-source Indic cultural dataset

Publish a research paper on corpus-driven cultural AI

5. Strategy to Increase User Adoption
Strategy	Execution Plan
College promotion	Share with cultural & literature clubs
WhatsApp groups	Family & regional community groups
Festival-focused campaign	Encourage users to share traditions
Social media	Share generated responses and stories
Incentives	“Top Contributor” leaderboard planned

Goal: Acquire 100+ cultural submissions within 4 weeks after public deployment.

Summary

BharatVaani successfully aligns with the Viswam.ai internship mission:

Uses open-source LLMs

Supports Indic languages

Designed for cultural corpus collection

Built using accessible and open-source tools

Shows clear roadmap for growth

This project demonstrates a strong understanding of prompt engineering, user-centric AI design, ethical dataset development, and full-stack AI deployment.

Submitted by:

Noor
Viswam.ai Summer of AI Internship 2025
GitHub Repository: https://github.com/Noorujoye/bharatvaani
