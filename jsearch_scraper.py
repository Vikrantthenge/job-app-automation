# jsearch_scraper.py
import requests

def fetch_jobs_jsearch(keyword, location, api_key, max_results=10):
    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": f"{keyword} in {location}",
        "num_pages": 1
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    jobs = []
    for job in data.get("data", [])[:max_results]:
        jobs.append({
            "title": job.get("job_title"),
            "company": job.get("employer_name"),
            "location": job.get("job_city"),
            "link": job.get("job_apply_link")
        })

    return jobs