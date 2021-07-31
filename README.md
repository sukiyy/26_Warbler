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

FLASK_ENV=production python -m unittest test_user_views.py
AttributeError: 'NoneType' object has no attribute 'likes'
----------------------------------------------------------------------
Ran 5 tests in 0.072s
FAILED (errors=1)


FLASK_ENV=production python -m unittest test_message_model.py
Ran 1 test in 0.023s
OK

FLASK_ENV=production python -m unittest test_message_views.py
Ran 1 test in 0.249s
OK


FLASK_ENV=production python -m unittest test_user_model.py
Ran 1 test in 0.018s
OK
