import streamlit as st
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM

BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "mental_health_bot"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map="auto")

def generate_reply(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output_ids = model.generate(**inputs, max_length=max_length, temperature=0.7)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

st.set_page_config(page_title="Mental Health Chatbot", page_icon="🧠")
st.title("🧠 Mental Health Support Chatbot")
st.write("This chatbot provides supportive and empathetic responses. It is **not** a therapist.")

user_input = st.text_input("How are you feeling today?")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        with st.spinner("Thinking..."):
            prompt = f"Context: \nUser: {user_input}\nEmotion: \nAgent:"
            response = generate_reply(prompt)
            st.success(response)
