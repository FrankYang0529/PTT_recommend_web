from subprocess import call
from lib.pttcrawler import PTTCrawler

ptt = PTTCrawler()
ptt.crawl()
ptt.export()
call(['mv', 'output.json', 'Article/new.json'])
