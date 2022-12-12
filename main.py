from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_tem = "python"

response = get(f"{base_url}{search_tem}")
if response.status_code != 200:
    print("Can't request website")
else:
    print(response.text)
