```
pip install -r .project/datacables/requirements/flask.txt
cd app
flask --app main.py db init
flask --app main.py db migrate
python main.py
```
