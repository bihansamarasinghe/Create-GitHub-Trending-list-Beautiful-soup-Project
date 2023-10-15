import requests
from bs4 import BeautifulSoup
import pprint

def get_trending_repositories():
    url_to_call = "https://github.com/trending"
    response = requests.get( url_to_call, headers={'user-agent':"MicrosoftEdge"})
    respose_code = response.status_code

    if respose_code != 200:
        print("Error Occured")
        return
    html_content = response.content
    #print(html_content)

    dom = BeautifulSoup(html_content,'html.parser')
    all_trending_repos = dom.select("article.Box-row h2")

    trending_repositories = []

    for each_trending_repo in all_trending_repos:
        href_link = each_trending_repo.a.attrs["href"]
        name = href_link[1:]
        repo = {"label": name, "link": "https://github.com{}".format(href_link)}
        trending_repositories.append(repo)

    return trending_repositories

    
if __name__ == "__main__":
    print("Started Scraping")
    trending_repos = get_trending_repositories()
    pprint.pprint(trending_repos)
