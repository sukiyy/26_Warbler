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

