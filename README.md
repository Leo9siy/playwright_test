# How to Run project
1. Clone repository to your computer
2. Create virtual environment
```commandline
python -m venv venv
```
3. Download all requirements
```commandline
pip install -r requirements.txt
```
4. Make .env file and fill the data from env_file
```commandline
touch .env
```
5. Run postgres
```commandline
docker-compose run --build
```
6. Run Django
```commandline
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
7. Try to save data
```commandline
python manage.py save_to_db
```