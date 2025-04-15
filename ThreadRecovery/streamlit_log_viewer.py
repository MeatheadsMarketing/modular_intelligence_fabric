
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Recovery Log Viewer", layout="wide")

st.title("🧠 GPT Thread Recovery – Log & Registry Viewer")

# Sidebar navigation
section = st.sidebar.selectbox("View Section", ["Thread Log", "Thread Registry", "Recovery Summary"])

base_path = "."

if section == "Thread Log":
    log_path = os.path.join(base_path, "logs", "thread_log.csv")
    if os.path.exists(log_path):
        df = pd.read_csv(log_path)
        st.subheader("📄 thread_log.csv")
        st.dataframe(df)
    else:
        st.warning("thread_log.csv not found.")

elif section == "Thread Registry":
    registry_path = os.path.join(base_path, "thread_registry.csv")
    if os.path.exists(registry_path):
        df = pd.read_csv(registry_path)
        st.subheader("📋 thread_registry.csv")
        st.dataframe(df)
    else:
        st.warning("thread_registry.csv not found.")

elif section == "Recovery Summary":
    summaries_dir = os.path.join(base_path, "recovered_threads")
    summaries = []

    if os.path.exists(summaries_dir):
        for subfolder in os.listdir(summaries_dir):
            summary_path = os.path.join(summaries_dir, subfolder, "recovery_summary.md")
            if os.path.exists(summary_path):
                with open(summary_path, "r") as f:
                    summaries.append((subfolder, f.read()))

    st.subheader("📝 Recovery Summaries")
    for name, content in summaries:
        with st.expander(name):
            st.markdown(content)
    if not summaries:
        st.info("No recovery summaries found.")
