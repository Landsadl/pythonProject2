import requests
from bs4 import BeautifulSoup
import pprint


response = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(response.text, 'html.parser')
links = (soup.select('.titleline'))
subtext = soup.select('.subtext')


def sort_stories(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_news(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].find('a').get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'Title': title, 'Links': href, 'votes': points})
    return sort_stories(hn)

#def filter_links(votes)

pprint.pprint(create_custom_news(links, subtext))