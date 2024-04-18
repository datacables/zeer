# ZEER
Data hooked on skeweres

```
pip install -r .project/datacables/requirements/flask.txt
cd app
cp settings.py.sample settings.py
flask --app main.py db init
flask --app main.py db migrate
flask --app main.py db upgrade
python main.py
```
