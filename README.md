# 📊 Strategic Tactic Generator (Streamlit App)

A web-based tool that helps pharma marketers select strategic challenges and tactic categories, then generates a list of recommended tactics with GPT-generated descriptions, suggested timelines, and budget estimates.

## 🚀 How to Use This App

1. Visit the live Streamlit app (once deployed)
2. Choose one or more **Strategic Challenges**
3. Choose one or more **Tactic Categories**
4. Click **Generate Plan** to see your custom tactical recommendations

## 🔐 Setting up your OpenAI API key

In the `.streamlit/secrets.toml` file, add your API key like this:

```
OPENAI_API_KEY = "your-openai-api-key-here"
```

## 📁 Project Structure
```
├── tactic_tool_streamlit.py
├── Strategic_Imperatives_Tactic_Matrix.xlsx
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml (user-created)
```

## 🧰 Requirements
- Python 3.8+
- Streamlit
- Pandas
- OpenAI
- openpyxl

## 💻 Run Locally
```bash
pip install -r requirements.txt
streamlit run tactic_tool_streamlit.py
```

## ☁️ Deploy on Streamlit Cloud
1. Push this code to a GitHub repo
2. Log in to https://streamlit.io/cloud with GitHub
3. Create a new app pointing to `tactic_tool_streamlit.py`
4. Done! Share the app with your team 🎉
