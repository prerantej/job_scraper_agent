# scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_jobs():
    url = "https://remoteok.com/remote-dev-jobs"  # Narrow category: dev jobs
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    job_cards = soup.find_all("tr", class_="job")  # Each job is a row with class "job"
    jobs = []

    for job in job_cards:
        try:
            title_tag = job.find("td", class_="company_and_position")
            title = title_tag.find("h2").text.strip() if title_tag else "N/A"
            company = title_tag.find("h3").text.strip() if title_tag else "N/A"
            location = job.find("div", class_="location").text.strip() if job.find("div", class_="location") else "Remote"
            date = job.find("time")['datetime'] if job.find("time") else "N/A"
            link = "https://remoteok.com" + job["data-href"] if job.has_attr("data-href") else "N/A"

            jobs.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Date": date,
                "Link": link
            })
        except Exception as e:
            print("Error parsing a job:", e)
            continue

    return jobs
