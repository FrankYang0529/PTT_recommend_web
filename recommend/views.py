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
        response_data_tmp = dict()
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
def relationship(request, user_name):
    # Get relationship by user
    if request.method == 'GET':
        response_data = dict()
        response_node = list()
        response_link = list()
        node_dict = dict()
        node_index = 1

        node_dict[user_name] = node_index
        node_index += 1
        response_node.append({"name": user_name, "group": 1})

        ptt_user_filter = PTT_User.objects.filter(user=user_name)
        if ptt_user_filter:
            for relation in ptt_user_filter[0].relations.all():
                reviewer = relation.friend
                if reviewer in node_dict:
                    pass
                else:
                    node_dict[reviewer] = node_index
                    node_index += 1
                    if relation.relationship == 0:
                        response_node.append({"name": reviewer, "group": 2})
                    elif relation.relationship > 0:
                        response_node.append({"name": reviewer, "group": 3})
                    else:
                        response_node.append({"name": reviewer, "group": 4})

                response_link.append({"source": node_dict[reviewer],
                                      "target": node_dict[user_name],
                                      "value": relation.relationship})

        relation_all = Relation.objects.filter(friend=user_name)
        for relation in relation_all:
            ptt_user = relation.ptt_user_set.all()[0]
            author = ptt_user.user
            if author in node_dict:
                pass
            else:
                node_dict[author] = node_index
                node_index += 1
                if relation.relationship == 0:
                    response_node.append({"name": author, "group": 2})
                elif relation.relationship > 0:
                    response_node.append({"name": author, "group": 3})
                else:
                    response_node.append({"name": author, "group": 4})
            response_link.append({"source": node_dict[user_name],
                                  "target": node_dict[author],
                                  "value": relation.relationship})

        response_data['nodes'] = response_node
        response_data['links'] = response_link
        return HttpResponse(json.dumps(response_data), content_type='application/json', status=200)
    else:
        return HttpResponse(status=400)
