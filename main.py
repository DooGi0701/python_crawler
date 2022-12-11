from requests import get

websites = [
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
]

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    print(response)  # Status Code
    if response.status_code >= 100 and response.status_code < 200:
        results[website] = "Information Code"
    elif response.status_code >= 200 and response.status_code < 300:
        results[website] = "Successful Code"
    elif response.status_code >= 300 and response.status_code < 400:
        results[website] = "Redirect Code"
    elif response.status_code >= 400 and response.status_code < 500:
        results[website] = "Client Error Code"
    elif response.status_code >= 500 and response.status_code < 600:
        results[website] = "Sever Error Code"
print(results)  # if문을 통해서 Status Code가 무슨 코드인지 알려주는 문구
