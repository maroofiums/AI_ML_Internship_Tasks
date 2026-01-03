import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = "./mental_health_bot"  

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

# Ensure pad token
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.eos_token_id

def generate_reply(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt")
    output_ids = model.generate(
        **inputs,
        max_length=max_length,
        do_sample=True,
        temperature=0.7
    )
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
