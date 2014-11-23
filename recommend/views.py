import sys
import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from recommend.models import Article, Review, Recommend_Author, PTT_User, Relation

@csrf_exempt
def recommend_article(request):
    # Get recommend article by user
    if request.method == 'POST':
        response_data = list()
        recommend_author_all = Recommend_Author.objects.filter(user=request.POST['user'])
        for recommend_author in recommend_author_all:
            response_data_tmp = dict()
            response_article = list()
            response_data_tmp['author'] = recommend_author.author
            article_all = Article.objects.filter(author=recommend_author)
            for article in article_all:
                response_article_tmp = model_to_dict(article, exclude=['author_title_date', 'author', 'ip', 'date', 'reviews'])
                response_article_tmp['date'] = str(article.date)
                response_review = list()
                for review in article.reviews.all():
                    response_review_tmp = model_to_dict(review, exclude=['date', 'id'])
                    response_review.append(response_review_tmp)
                response_article_tmp['review'] = response_review
                response_article.append(response_article_tmp)
                break
            response_data_tmp['article'] = response_article
            break
        response_data.append(response_data_tmp)
        return HttpResponse(json.dumps(response_data), content_type='application/json', status=200)
    else:
        return HttpResponse(status=400)

@csrf_exempt
def relationship(request):
    # Get relationship by user
    if request.method == 'POST':
        response_data = dict()
        response_indegree = list()
        response_outdegree = list()
        user = PTT_User.objects.filter(user=request.POST['user'])
        if user:
            for relation in user[0].relations.all():
                response_data_tmp = model_to_dict(relation, exclude=['id'])
                response_indegree.append(response_data_tmp)

        relation_all = Relation.objects.filter(friend=request.POST['user'])
        for relation in relation_all:
            for ptt_user in relation.ptt_user_set.all():
                response_data_tmp = {'user': ptt_user.user,
                                     'relationship': relation.relationship}
                response_outdegree.append(response_data_tmp)

        response_data['indegree'] = response_indegree
        response_data['outdegree'] = response_outdegree
        return HttpResponse(json.dumps(response_data), content_type='application/json', status=200)
    else:
        return HttpResponse(status=400)
