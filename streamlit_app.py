import streamlit as st
from tsb_generator import generate_tsb_with_ollama
from fpdf import FPDF

# Load prompt template once
with open("tsb_prompt.txt", "r") as file:
    prompt_template = file.read()

st.set_page_config(page_title="AI-Generated TSBs", layout="wide")

st.title("🚗 AI-Generated Technical Service Bulletins (TSBs) for EVs")
st.markdown("Upload a repair log below and generate a TSB using local LLMs (Ollama).")

uploaded_file = st.file_uploader("📄 Upload a repair log (.txt)", type="txt")

def create_pdf(text: str) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.cell(0, 10, txt=line, ln=True)
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    return pdf_bytes

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

                # Markdown download button
                st.download_button(
                    label="💾 Download TSB (.md)",
                    data=tsb,
                    file_name="generated_tsb.md",
                    mime="text/markdown"
                )

                # PDF download button
                pdf_bytes = create_pdf(tsb)
                st.download_button(
                    label="📄 Download TSB as PDF",
                    data=pdf_bytes,
                    file_name="generated_tsb.pdf",
                    mime="application/pdf"
                )

            except Exception as e:
                st.error(f"❌ Error generating TSB: {e}")

else:
    st.info("Please upload a repair log file to get started.")

