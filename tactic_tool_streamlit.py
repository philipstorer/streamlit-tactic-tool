import streamlit as st
import pandas as pd

# Load data
file_path = "./Strategic_Imperatives_Tactic_Matrix.xlsx"
df = pd.read_excel(file_path)

# Get unique values
strategic_challenges = df['Strategic Challenge'].dropna().unique().tolist()
tactic_categories = df.columns[1:].tolist()

# Description generator
def generate_description(tactic):
    if pd.isna(tactic):
        return None
    description = f"'{tactic}' is a tactic focused on driving engagement or solving specific friction points. It works well in targeted educational campaigns or behavior reinforcement programs."
    return {
        "name": tactic,
        "description": description,
        "timeframe": "4–8 weeks",
        "budget": "$15K–$50K"
    }

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
        output = []
        for _, row in filtered_df.iterrows():
            for category in selected_categories:
                tactic = row.get(category)
                result = generate_description(tactic)
                if result:
                    output.append(result)

        if output:
            st.subheader("Recommended Tactics")
            for item in output:
                st.markdown(f"### {item['name']}")
                st.write(item['description'])
                st.write(f"**Timeframe:** {item['timeframe']}")
                st.write(f"**Budget:** {item['budget']}")
                st.markdown("---")
        else:
            st.info("No tactics matched your criteria.")
