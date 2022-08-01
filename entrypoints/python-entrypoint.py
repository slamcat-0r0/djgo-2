import os



if __name__ == "__main__":
    os.system("python3 manage.py makemigrations")
    os.system("python3 manage.py migrate")
    os.system(f"python3 manage.py runserver 0.0.0.0:{os.environ.get('DJGO_OPORT')}")