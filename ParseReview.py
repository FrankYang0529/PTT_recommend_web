from subprocess import call
from lib.pttcrawler import PTTCrawler

ptt = PTTCrawler()
ptt.crawl(start=5000)
ptt.export()
call(['mv', 'output.json', 'Article/5000.json'])

