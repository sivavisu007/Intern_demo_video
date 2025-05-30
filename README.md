# 🧠 HSN Code Validation and Suggestion Agent (Google ADK)

This project implements an intelligent agent using the **Google Agent Developer Kit (ADK)** that can:

✅ Validate HSN codes based on structure and existence in a master dataset  
🔍 Suggest appropriate HSN codes based on a user-provided product or service description

---

## 📁 Project Structure

hsn-adk-agent/
├── data/
│ └── HSN_SAC.xlsx # Master dataset
├── agent/
│ ├── hsn_agent.py # ADK agent wrapper
│ ├── validate_plan.py # Plan for validating HSN codes
│ ├── suggest_plan.py # Plan for suggesting HSN codes
│ └── utils.py # Data loading utilities
├── screenshots/
│ └── results.png # Output screenshots
├── main.py # Application entry point
├── requirements.txt # Dependencies
└── README.md # This file

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hsn-adk-agent.git
cd hsn-adk-agent
2. Install Dependencies
bash
pip install -r requirements.txt
3. Run the Agent
bash
python main.py
🧪 Features Demonstrated
✅ HSN Code Validation
Checks format (2–8 digits, numeric)

Validates if code exists in dataset

Verifies parent-level hierarchy codes (e.g., 01, 0101 for 01011010)

🔍 HSN Code Suggestion
Based on partial or full product descriptions

Returns most relevant HSN codes with descriptions

🖼️ Output Screenshots
1. Validation Output

2. Suggestion Output

📹 Demo Video
Watch the complete demo video here:
📎 Google Drive Demo Link

📊 Dataset
The master HSN dataset is available in the data/ directory as:

HSN_SAC.xlsx

It contains two columns:

HSNCode – The code (e.g., 0101, 01011010)

Description – Goods or service description

🧠 Technologies Used
Google ADK (Agent Developer Kit)

Python 3

pandas, openpyxl

🙌 Acknowledgements
Special thanks to the evaluation team for the assignment brief and support.

📬 Contact
Developed by SIVAHARI V
📧 Email: sivavisu71@gmail.com
🔗 GitHub: https://github.com/sivavisu007
