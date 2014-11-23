import os
import json
import django
from recommend.models import Article

os.environ["DJANGO_SETTINGS_MODULE"] = "PTT_web.settings"
django.setup()

reviewer_author_csv = open("reviewer_author.csv", "w")
user_dict = dict()
reviewer_author_dict = dict()
user_index = 1

article_all = Article.objects.all()
for article in article_all:
    author = article.author
    if author in user_dict:
        pass
    else:
        user_dict[author] = user_index
        user_index += 1

    review_all = article.reviews.all()
    for review in review_all:
        reviewer = review.reviewer
        if reviewer in user_dict:
            pass
        else:
            user_dict[reviewer] = user_index
            user_index += 1

        reviewer_author = reviewer + ' ' + author
        if reviewer_author in reviewer_author_dict:
            pass
        else:
            reviewer_author_dict[reviewer_author] = 0

        if review.status == '推':
            reviewer_author_dict[reviewer_author] += 2
        elif review.status == '噓':
            reviewer_author_dict[reviewer_author] -= 2
        else:
            reviewer_author_dict[reviewer_author] += 1

with open("user.json", "w") as f:
    json.dump(user_dict, f, ensure_ascii=False, indent=4, sort_keys=True)

with open("reviewer_author.json", "w") as f:
    json.dump(reviewer_author_dict, f, ensure_ascii=False, indent=4, sort_keys=True)

for key in sorted(reviewer_author_dict.keys()):
    reviewer = key.split()[0]
    author = key.split()[1]
    reviewer_author_csv.write(str(user_dict[reviewer]) + "," + str(user_dict[author]) + "," + str(reviewer_author_dict[key]) + "\n")

reviewer_author_csv.close()
