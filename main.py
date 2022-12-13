from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_tem = "python"

response = get(f"{base_url}{search_tem}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.find_all("title"))
