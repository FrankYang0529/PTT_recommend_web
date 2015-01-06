import os
import json
import django
from datetime import datetime
from recommend.models import Article, Review

os.environ['DJANGO_SETTINGS_MODULE'] = 'PTT_web.settings'
django.setup()

json_file = open('Article/5000.json')
load_file = json.load(json_file)

for article_data in load_file:
    author = article_data['b_作者'].split('(')[0]
    title = article_data['c_標題']
    date_str = article_data['d_日期']
    author_title_date = author + ' ' + title + ' ' + date_str

    article_filter = Article.objects.filter(author_title_date=author_title_date)
    if article_filter:
        article = article_filter[0]
    else:
        try:
            date = datetime.strptime(date_str, '%a %b %d %H:%M:%S %Y')
        except:
            date = datetime.now()

        if article_data['e_ip'] == 'ip is not find':
            ip = ''
        else:
            ip = article_data['e_ip']

        article = Article(author_title_date=author_title_date,
                          author=author,
                          title=title,
                          content=article_data['f_內文'],
                          ip=ip,
                          date=date)
        article.save()

    for review_data in article_data['g_推文']:
        if review_data['留言內容']:
            review_content = ''
        else:
            review_content = review_data['留言內容'][1:]
        review_filter = Review.objects.filter(reviewer=review_data['留言者'],
                                              message=review_content,
                                              status=review_data['狀態'],
                                              date=review_data['留言時間'])
        if review_filter:
            pass
        else:
            review = Review(reviewer=review_data['留言者'],
                            message=review_content,
                            status=review_data['狀態'],
                            date=review_data['留言時間'])
            review.save()
            article.reviews.add(review)
