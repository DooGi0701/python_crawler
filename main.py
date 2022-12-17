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
        job_posts.pop(-1)  # 출력항목에 있는 마지막 항목을 제거한다.
        for post in job_posts:
            anchors = post.find_all("a")  # html안에 있는 li안에 있는 하이퍼링크 부분을 찾아라
            anchor = anchors[1]  # 찾은 하이퍼 링크 부분 중 두번째 자리 부분을 대입하라
            link = anchor[
                "href"
            ]  # href에 접근할 수 있다 Tip : beautiful Soup는 html에 있는 태그들을 파이썬에 있는 dirtionary 처럼 바꿔 줄 수 있다
            # link를 print로 바꾸면 출력물을 볼 수 있음
