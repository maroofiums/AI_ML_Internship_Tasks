from pathlib import Path
import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

st.set_page_config(page_title="Mental Health Support Chatbot")

BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "mental_health_bot"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        device_map="auto"
    )
    return tokenizer, model

tokenizer, model = load_model()

st.title("Mental Health Support Chatbot")

user_input = st.text_input("How are you feeling today?")

if user_input:
    prompt = f"User: {user_input}\nAgent:"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_length=150,
        temperature=0.7,
        do_sample=True
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    st.write(response)
