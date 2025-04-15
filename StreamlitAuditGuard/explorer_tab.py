
import streamlit as st
import pandas as pd
import os

def load_registry():
    registry_path = os.path.join(os.path.dirname(__file__), "..", "data", "v1_master_registry.csv")
    if not os.path.exists(registry_path):
        st.warning("Registry file not found.")
        return pd.DataFrame()
    return pd.read_csv(registry_path)

def main():
    st.title("Assistant Explorer – Registry View")

    df = load_registry()
    if df.empty:
        return

    # Optional filters
    with st.sidebar:
        tag_filter = st.selectbox("Filter by Tag", ["All"] + sorted(df["Tag"].dropna().unique()))
        status_filter = st.selectbox("Filter by Fix Status", ["All"] + sorted(df["Fix_Status"].dropna().unique()))

    filtered = df.copy()
    if tag_filter != "All":
        filtered = filtered[filtered["Tag"] == tag_filter]
    if status_filter != "All":
        filtered = filtered[filtered["Fix_Status"] == status_filter]

    st.dataframe(filtered, use_container_width=True)


    st.markdown("### Launchable Assistants")

    for i, row in filtered.iterrows():
        if row.get("Final_Status") == "Ready":
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"{row['Code']}: {row['Name']}")
            with col2:
                if st.button(f"Launch", key=f"launch_{row['Code']}"):
                    st.success(f"Launching {row['Code']}... (simulation)")
                    # Replace this with actual launch logic (e.g., subprocess or routing)


    # Optional preview
    with st.expander("Preview First Row"):
        st.json(filtered.iloc[0].to_dict() if not filtered.empty else {})
