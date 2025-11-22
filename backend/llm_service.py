import os
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from .prompts import SYSTEM_PROMPT

load_dotenv()

# Load Hugging Face Token
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

# Choose model (good Hindi performance)
MODEL_ID = "google/gemma-2b-it"   # fallback options: mistralai/Mistral-7B-Instruct-v0.2  or  meta-llama/Llama-2-7b-chat-hf

# Prompt Template
prompt = PromptTemplate(
    input_variables=["query"],
    template=SYSTEM_PROMPT + "\n\nUser: {query}\nAssistant:"
)

# LLM Wrapper
llm = HuggingFaceHub(
    repo_id=MODEL_ID,
    huggingfacehub_api_token=HF_TOKEN,
    model_kwargs={"temperature": 0.5, "max_new_tokens": 450}
)

# LangChain Execution Function
def generate_response(query: str):
    try:
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(query)
        return response.strip()
    except Exception as e:
        return f"⚠️ Model Error: {e}"
