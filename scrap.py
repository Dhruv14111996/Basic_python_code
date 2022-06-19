import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body)
# print(soup.find_all('div'))
links = soup.select('.titlelink')
subtext = soup.select('.subtext')
# print(votes[0])


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['vote'], reverse=True)


def creat_custom_hn(links, subtext):
    hn = []
    for indx, item in enumerate(links):
        title = item.getText()
        href = item.get('href')
        vote = subtext[indx].get('.score')
        if vote:
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'links': href, 'votes': points})
        return hn


print(creat_custom_hn(links, subtext))
