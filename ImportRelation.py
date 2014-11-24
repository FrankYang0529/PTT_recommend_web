import json
import django
from recommend.models import PTT_User, Relation

django.setup()
json_file = open('reviewer_author.json')
load_file = json.load(json_file)

for key in sorted(load_file.keys()):
    reviewer = key.split()[0]
    author = key.split()[1]
    user_filter = PTT_User.objects.filter(user=author)
    if user_filter:
        ptt_user = PTT_User.objects.get(user=author)
        relation = Relation(friend=reviewer,
                            relationship=int(load_file[key]))
        relation.save()
        ptt_user.relations.add(relation)
    else:
        ptt_user = PTT_User(user=author)
        ptt_user.save()
        relation = Relation(friend=reviewer,
                            relationship=int(load_file[key]))
        relation.save()
        ptt_user.relations.add(relation)

