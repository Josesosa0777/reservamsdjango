# Create environment and activate it
```
python3 -m venv venv    #virtualenv newvenv -p python3.10
. venv/bin/activate
```
Download postgress
https://www.postgresql.org/download/macosx/ para instalarlo, pero se puede con homebrew.  
password: 0713 port: 5432

        #brew install postgresql
        #brew services start postgresql 
        #brew services restart rabbitmq

en folder de proyecto:
```
export PATH=$PATH:/Library/PostgreSQL/14/bin
pip3.10 install --upgrade wheel # si se tiene python 3.10
pip3.10 install --upgrade setuptools
pip3.10 install psycopg2

pip3 install -r requirements.txt
```




## 2022 Mayo
use *from django.utils.translation import gettext_lazy as _* instead of 
*from django.utils.translation import ugettext_lazy as _*

en file .env:
´´´
DJANGO_SECRET_KEY='django-insecure-@+67+y+e0plh_zm)8nk8chmefs4e1z^r4yz4nbh1&sh*s1d#0#'
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=[]
´´´

run:
export DJANGO_SETTINGS_MODULE=reservperformance.settings
python manage.py runserver    

#pasar debug a false
