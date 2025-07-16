import streamlit as st
import os
from tsb_generator import generate_tsb_with_ollama

# Load prompt template
with open("tsb_prompt.txt", "r") as file:
    prompt_template = file.read()

st.set_page_config(page_title="AI-Generated TSBs", layout="wide")

st.title("🚗 AI-Generated Technical Service Bulletins (TSBs) for EVs")
st.markdown("Upload a repair log below and generate a TSB using local LLMs (Ollama).")

uploaded_file = st.file_uploader("📄 Upload a repair log (.txt)", type="txt")

if uploaded_file:
    repair_log = uploaded_file.read().decode("utf-8")
    st.subheader("📋 Repair Log Preview")
    st.code(repair_log, language="text")

    if st.button("Generate TSB"):
        with st.spinner("Generating TSB using Ollama..."):
            try:
                tsb = generate_tsb_with_ollama(repair_log, prompt_template)
                st.success("✅ TSB Generated!")
                st.subheader("🧾 TSB Output")
                st.markdown(tsb)

                st.download_button("💾 Download TSB (.md)", tsb, file_name="generated_tsb.md")
            except Exception as e:
                st.error(f"❌ Error: {e}")
