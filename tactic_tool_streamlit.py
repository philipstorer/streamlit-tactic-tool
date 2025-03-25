import streamlit as st
import pandas as pd
import openai
import os

# Load data
file_path = "./Strategic_Imperatives_Tactic_Matrix.xlsx"
df = pd.read_excel(file_path)

# Get unique values
strategic_challenges = df['Strategic Challenge'].dropna().unique().tolist()
tactic_categories = df.columns[1:].tolist()

# Description, timeframe, and budget generator using GPT
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt_estimates(tactic):
    prompt = f"""
    For the following pharmaceutical marketing tactic, provide:
    1. A 2-3 sentence description
    2. An estimated execution timeline (in weeks)
    3. A typical budget range (USD)

    Tactic: {tactic}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Description unavailable. Error: {e}"

# UI
st.title("Strategic Tactic Generator")
st.markdown("Select your strategic challenges and tactic categories to generate a custom execution plan.")

selected_challenges = st.multiselect("Select Strategic Challenges", strategic_challenges)
selected_categories = st.multiselect("Select Tactic Categories", tactic_categories)

if st.button("Generate Plan"):
    if not selected_challenges or not selected_categories:
        st.warning("Please select at least one challenge and one category.")
    else:
        filtered_df = df[df['Strategic Challenge'].isin(selected_challenges)]
        seen_tactics = set()
        results_by_challenge = {}

        for challenge in selected_challenges:
            challenge_df = filtered_df[filtered_df['Strategic Challenge'] == challenge]
            unique_tactics = []

            for _, row in challenge_df.iterrows():
                for category in selected_categories:
                    tactic = row.get(category)
                    if pd.notna(tactic) and tactic not in seen_tactics:
                        seen_tactics.add(tactic)
                        unique_tactics.append(tactic)

            results = []
            for tactic in unique_tactics:
                gpt_result = get_gpt_estimates(tactic)
                results.append((tactic, gpt_result))

            results_by_challenge[challenge] = results

        # Display Results
        for challenge, tactics in results_by_challenge.items():
            st.subheader(f"Strategic Challenge: {challenge}")
            for name, result in tactics:
                st.markdown(f"### {name}")
                st.markdown(result)
                st.markdown("---")
