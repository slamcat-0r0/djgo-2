import os
import socket
import time






if __name__ == "__main__":

    os.system("python3 manage.py makemigrations")
    os.system("python3 manage.py migrate")
    os.system("python3 manage.py collectstatic --noinput")
    cmd = f"echo \"from django.contrib.auth.models import User; User.objects.create_superuser('{os.environ.get('DJGO_ADMIN_LOGIN')}', '{os.environ.get('DJGO_ADMIN_EMAIL')}', '{os.environ.get('DJGO_ADMIN_PASSWD')}')\" | python3 manage.py shell"
    print("Creating superuser...")
    os.system(cmd)

    # DEV
    os.system(f"python3 manage.py runserver 0.0.0.0:{os.environ.get('DJGO_OPORT')}")

    # PROD
    # os.system(f"gunicorn --bind 0.0.0.0:{os.environ.get('DJGO_OPORT')} project.wsgi")

    time.sleep(1)



    