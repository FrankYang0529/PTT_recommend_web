cd /home/ubuntu/PTT_web
export DJANGO_SETTINGS_MODULE=PTT_web.settings
python3.4 ParseDB.py
AWS_ACCESS_KEY_ID=AKIAI32KTOZXIDMB3Z7A AWS_SECRET_ACCESS_KEY=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 aws s3 cp reviewer_author.csv s3://pttweb/reviewer_author.csv
cd /home/ubuntu/spark
python spot-script.py
cd /home/ubuntu/PTT_web
rm -rf Recommend/
AWS_ACCESS_KEY_ID=AKIAI32KTOZXIDMB3Z7A AWS_SECRET_ACCESS_KEY=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 aws s3 cp s3://pttweb/Recommend Recommend/ --recursive

AWS_ACCESS_KEY_ID=AKIAI32KTOZXIDMB3Z7A AWS_SECRET_ACCESS_KEY=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 aws s3 rm s3://pttweb --recursive
