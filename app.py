# app.py

import streamlit as st
import pandas as pd
from scraper import scrape_jobs

st.title("💼 Job Scraper Agent (RemoteOK)")

if st.button("Scrape Jobs"):
    jobs = scrape_jobs()
    st.session_state.jobs = jobs
    st.success(f"Scraped {len(jobs)} jobs!")

# Show only if jobs are already scraped
if 'jobs' in st.session_state:
    df = pd.DataFrame(st.session_state.jobs)

    # Filters
    keyword = st.text_input("🔍 Filter by keyword (e.g. Python, React):")
    location = st.text_input("📍 Filter by location (e.g. Europe, Remote):")

    filtered_df = df
    if keyword:
        filtered_df = filtered_df[filtered_df['Title'].str.contains(keyword, case=False)]
    if location:
        filtered_df = filtered_df[filtered_df['Location'].str.contains(location, case=False)]

    st.write("### 📝 Filtered Job Listings")
    st.dataframe(filtered_df)

    st.download_button("📥 Download CSV", filtered_df.to_csv(index=False), "jobs.csv")
