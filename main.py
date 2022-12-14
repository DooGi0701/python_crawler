from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_tem = "python"

response = get(f"{base_url}{search_tem}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all(
        "section", class_="jobs"
    )  # 결과 값을 보고 싶으면 맨 앞에 있는 jobs=를 print()로 바꿔라
    for job_section in jobs:
        job_posts = job_section.find_all("li")
