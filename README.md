# 26_Warbler

1. FIND FOLDER AND CREATE VERV FOLDER:
python3 -m venv venv
source venv/bin/activate

2. INSTALL REQUIREMENTS:
pip3 install -r requirements.txt

3. CREATE DATABASE WARBLER:
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/12/bin
PSQL
create database warbler;

4. run seeds file:
python3 seeds.py

5. run flask:
FLASK_ENV=development flask run
export FLASK_ENV=development

-----------
<img width="1273" alt="Screen Shot 2021-07-31 at 3 00 38 PM" src="https://user-images.githubusercontent.com/37279343/127749973-5103a98b-e24d-4ca5-af1f-afa4802c0aae.png">
<img width="1275" alt="Screen Shot 2021-07-31 at 2 58 43 PM" src="https://user-images.githubusercontent.com/37279343/127749976-4227ffc9-1cbb-4cd5-a173-d58e495b7bc4.png">
<img width="1272" alt="Screen Shot 2021-07-31 at 2 58 57 PM" src="https://user-images.githubusercontent.com/37279343/127749977-244a540b-2f93-4f65-9127-ab68c3b858d5.png">
<img width="1274" alt="Screen Shot 2021-07-31 at 2 59 15 PM" src="https://user-images.githubusercontent.com/37279343/127749979-eab55e97-a0d7-4390-9ac2-7e26fcf2277e.png">
<img width="1277" alt="Screen Shot 2021-07-31 at 2 59 29 PM" src="https://user-images.githubusercontent.com/37279343/127749980-60c097a8-ec4a-4b2a-8b33-215211c2dc44.png">
<img width="1274" alt="Screen Shot 2021-07-31 at 2 59 42 PM" src="https://user-images.githubusercontent.com/37279343/127749981-96ba8416-245e-4377-a789-3e2940aec8ef.png">
<img width="1275" alt="Screen Shot 2021-07-31 at 2 59 54 PM" src="https://user-images.githubusercontent.com/37279343/127749982-3ecbb61f-cf4f-40a6-a5de-6b6414b11702.png">

-----------

FLASK_ENV=production python -m unittest test_user_views.py
Ran 4 tests in 0.072s
OK


FLASK_ENV=production python -m unittest test_message_model.py
Ran 1 test in 0.023s
OK

FLASK_ENV=production python -m unittest test_message_views.py
Ran 1 test in 0.249s
OK


FLASK_ENV=production python -m unittest test_user_model.py
Ran 1 test in 0.018s
OK
