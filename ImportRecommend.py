import os
import json
import django
from recommend.models import Recommend_Author

os.environ['DJANGO_SETTINGS_MODULE'] = 'PTT_web.settings'
django.setup()

user_int_json = json.load(open('user.json'))
int_user_dict = dict()
for user in user_int_json:
    int_user_dict[user_int_json[user]] = user

for dirPath, dirNames, fileNames in os.walk('tmp/'):
    for f in fileNames:
        if f[0] == '.':
            pass
        elif f == '_SUCCESS':
            pass
        else:
            dirFile = os.path.join(dirPath, f)
            print (dirFile)
            partFile = open(dirFile, 'r')
            while True:
                s = partFile.readline()
                if s == '':
                    break
                else:
                    score = float(s.split('(')[1].split(',')[2].split(')')[0])
                    if score >= 1.9:
                        user_int = s.split('(')[1].split(',')[0]
                        user_str = int_user_dict[int(user_int)]
                        author_int = s.split('(')[1].split(',')[1]
                        author_str = int_user_dict[int(author_int)]
                        recommend_author = Recommend_Author(user=user_str,
                                                            author=author_str,
                                                            score=score)
                        recommend_author.save()
            partFile.close()
