# itudb2211 - PLStats
PLStads is a web application for performing CRUD operations with the data of the English football league, the Premier League.

PLStats developed by Mehmet Emre Topdal, Bilge Kır and Barış Kerem Hüseyinoğlu for ITU / BLG317 course.

PLStats uses Python/Flask, WTForms, Bootstrap and SQL/Sqlite3

The tables in the application are linked to the same table as the foreign keys, namely the "TEAMS" table. Therefore, 6 f-keys were created, 2 for each team member.

## Team members roles
Mehmet Emre Topdal: Responsible for TEAMS, ATTACK and ATTEMPTS tables. The frontend codes associated with these tables belong to him. He also prepared "index.html" and error handling logic and "error.html" pages.

## to run app, use commands below:

py -3 -m venv venv

venv\Scripts\activate

pip install Flask

pip install WTForms

python server.py

## photos from demo


![indexxx](https://user-images.githubusercontent.com/108151964/208299599-cdf0c5ae-f13c-49d8-8f0c-983b02693229.PNG)
**********************************************************
![tablolar](https://user-images.githubusercontent.com/108151964/208299607-2f2c3d63-7aac-41e3-8ae2-99e3d4c6aaf5.PNG)
**********************************************************
![form](https://user-images.githubusercontent.com/108151964/208299619-a88c32f5-3a93-4aa9-8e05-ca202ee3a360.PNG)
**********************************************************
![error](https://user-images.githubusercontent.com/108151964/208299624-8e54e46d-8d0c-4352-a9e9-b26149115516.PNG)

