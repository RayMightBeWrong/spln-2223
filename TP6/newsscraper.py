#!/usr/bin/python3

import newspaper
import os

path = os.getcwd()

url = 'https://www.monitor.co.ug/uganda'

jn = newspaper.build(url)

if not os.path.exists('/tmp/.newspaper_scraper'):
    newpath = f'{path}/newspaper_scraper'
    os.symlink(newpath, '/tmp/.newspaper_scraper')


for article in jn.articles:
    ar = newspaper.Article(article.url)
    ar.download()
    ar.parse()
    print(f'''
<article>
    <title>{ar.title}</title>
    <url>{ar.url}</url>
    <author>{ar.authors}</author>
    <date>{ar.publish_date}</date>
    <text>{ar.text}</text>
<article>
''')
