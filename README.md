# 🔧 AI-Generated Technical Service Bulletins (TSBs) for EVs

This project uses local LLMs to automatically generate Technical Service Bulletins (TSBs) from electric vehicle (EV) repair logs. It includes clustering similar logs, generating markdown TSBs, and a user-friendly Streamlit interface.

---

## 🚀 Features

- ⚙️ **TSB Generation** using local LLMs (e.g. Mistral via Ollama)
- 🧠 **Unsupervised Clustering** of similar repair logs
- 📄 **Markdown Export** of generated TSBs
- 🎛️ **Streamlit Web App** for interactive use
- 🔌 **Offline Compatible** – no API calls or internet required
- 🗃️ Organized project structure with extensible modules

---

## 📁 Project Structure

AI-Generated-TSBs-for-Evs/
│
├── app/ # App logic & modules
│ ├── init.py # (optional for now)
│ ├── tsb_generator.py # Core logic for TSB generation with Ollama
│ ├── clustering.py # (optional: for clustering logic)
│ ├── utils.py # (optional: helper functions)
│
├── data/ # Input data files
│ ├── repair_logs_sample.txt # Sample repair logs
│ ├── tsb_prompt.txt # Prompt template for TSB generation
│ └── clustered_logs/ # Logs grouped by similarity
│ ├── cluster_1.txt
│ └── ...
│
├── outputs/ # Final generated outputs
│ ├── Tsbs/ # Markdown TSBs
│ └── generated_tsb_clusters/ # Clustered summaries
│
├── scripts/ # Python scripts for generation & clustering
│ ├── generate_tsb.py
│ ├── cluster_logs.py
│ ├── generate_cluster_tsbs.py
│ └── batch_generate.py
│
├── streamlit_app.py # Streamlit interface for generating TSBs
├── requirements.txt # Python dependencies
├── README.md # You're here
└── venv/ # Virtual environment (excluded from version control)

yaml
Copy
Edit

---

## 🛠️ Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed locally
- A local LLM (e.g., `mistral`, `llama3`, `phi3`)
- pip packages:
  - `streamlit`
  - `scikit-learn`
  - `numpy`
  - `pandas`
  - `ollama`

---

## To install and start Ollama:

Install Ollama:

```bash
brew install ollama
Download and run a model (e.g. Mistral):

bash
Copy
Edit
ollama run mistral
Make sure the model is running before launching the app or scripts.

📦 Installation
Clone and set up the project:

bash
Copy
Edit
git clone https://github.com/your-username/AI-Generated-TSBs-for-Evs.git
cd AI-Generated-TSBs-for-Evs
Create a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install Python dependencies:

bash
Copy
Edit
pip install -r requirements.txt
⚙️ How to Run the Scripts
1. Generate TSBs from Raw Logs
bash
Copy
Edit
python3 scripts/generate_tsb.py
📂 Output: outputs/Tsbs/tsb_1.md, tsb_2.md, etc.

2. Cluster Logs into Groups
bash
Copy
Edit
python3 scripts/cluster_logs.py
📂 Output: data/clustered_logs/cluster_1.txt, cluster_2.txt, etc.

3. Generate TSBs from Clustered Logs
bash
Copy
Edit
python3 scripts/generate_cluster_tsbs.py
📂 Output: outputs/Tsbs/cluster_1.md, etc.

4. Launch the Streamlit App
bash
Copy
Edit
streamlit run streamlit_app.py
Then open http://localhost:8501 in your browser.

🧪 Sample File Format
repair_logs_sample.txt example:

yaml
Copy
Edit
Vehicle Model X shuts down randomly while charging.
Charging port light flashes red, indicating failure.
---

Battery temperature spikes above 70°C under low load.
Frequent system reboots observed after power drain.
Each log is separated by either a double newline or ---.

🧠 Model & Prompt
The prompt used for TSB generation is stored in:

bash
Copy
Edit
data/tsb_prompt.txt
It provides instructions to the LLM for generating concise, technical, and standardized service bulletins based on the input logs.

You can customize the prompt to match your formatting preferences or tone of voice.

✅ Current Status
✅ Offline TSB generation using Ollama

✅ Clustering of logs for grouped TSBs

✅ Markdown file generation for each TSB

✅ Streamlit UI for manual upload and generation

🔜 Export to PDF (Planned)

🔜 Add quality evaluation & ranking (Planned)

🔜 Multi-log summarization via embedding clustering (Planned)

🙌 Acknowledgments
Ollama – local LLM orchestration

scikit-learn – clustering engine

Streamlit – web app UI

✍️ Author
Iftekhar Ahmed
Berlin, Germany
AI | ML | Automation | Sustainability
