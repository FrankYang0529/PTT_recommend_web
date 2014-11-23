from subprocess import call
from lib.pttcrawler import PTTCrawler

ptt = PTTCrawler()
ptt.crawl(start=4500)
ptt.export()
call(['mv', 'output.json', 'Article/4500.json'])

