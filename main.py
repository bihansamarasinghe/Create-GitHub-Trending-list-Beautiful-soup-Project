import requests  # Importing the requests library for making HTTP requests
from bs4 import BeautifulSoup  # Importing BeautifulSoup for HTML parsing
import pprint  # Importing pprint for pretty-printing data structures

def get_trending_repositories():
    url_to_call = "https://github.com/trending"  # URL of the GitHub trending page
    response = requests.get(url_to_call, headers={'user-agent': 'MicrosoftEdge'})  # Sending a GET request to the URL
    response_code = response.status_code  # Getting the HTTP response status code

    if response_code != 200:  # Checking if the response status is not 200 (OK)
        print("Error Occurred")  # Printing an error message
        return []  # Returning an empty list if an error occurred

    html_content = response.content  # Getting the content of the response
    dom = BeautifulSoup(html_content, 'html.parser')  # Parsing the HTML content
    all_trending_repos = dom.select("article.Box-row h2")  # Selecting all h2 elements within article.Box-row

    trending_repositories = []  # Initializing a list to store trending repositories

    for each_trending_repo in all_trending_repos:  # Iterating through each trending repository element
        href_link = each_trending_repo.a.attrs["href"]  # Extracting the href attribute (repository link)
        name = href_link[1:]  # Extracting the repository name
        repo = {"label": name, "link": "https://github.com{}".format(href_link)}  # Creating a dictionary with repository label and link
        trending_repositories.append(repo)  # Appending the repository dictionary to the list

    return trending_repositories  # Returning the list of trending repositories

if __name__ == "__main__":
    print("Started Scraping")  # Printing a message indicating the start of scraping
    trending_repos = get_trending_repositories()  # Getting the trending repositories
    pprint.pprint(trending_repos)  # Pretty-printing the trending repositories
