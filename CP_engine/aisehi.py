import requests
from bs4 import BeautifulSoup
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', "CP_engine.settings")

import django
django.setup()

from engine.models import problem


for i in range(8, 10):
    url = "https://codeforces.com/problemset/page/"+str(i)
    r = requests.get(url)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')
    anchors = soup.find_all('a')
    all_links = dict()
    k=1
    for link in anchors:
        if(link.get('href')[1:19] == 'problemset/problem'): 
            linkText = "https://codeforces.com" + link.get('href')
            if(len(link.string.split('\r\n'))!=3):
                all_links[linkText]=link.string.split('\r\n')[1]
                name = link.string.split('\r\n')[1]
                proburl = linkText
                s=requests.get(proburl)
                probcontent = s.content
                newsoup = BeautifulSoup(probcontent, 'html.parser')
                s = ""
                tags = newsoup.find_all(class_="tag-box")
                for tag in tags:
                    s=s+" "+tag.string.strip()
                prob_tags = s[1:]
                contest = link.get('href')[20:]
                searchs=name+prob_tags+proburl
                print(linkText)
                new_prob = problem.objects.create(name=name, url=proburl, tag=prob_tags, contest=contest, search=searchs)
                new_prob.save()


