netstat -ltnup | grep :8000 | tr "/" "\n" | head -1 | tr " " "\n" | tail -1 | xargs kill -9

python manage.py runserver