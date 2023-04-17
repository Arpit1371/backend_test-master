given employee can be searched and change company

# run following commands in terminalinbackend_test directory 
# after cloning.

pip install pipenv
pipenv install
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
# this command could take some time to run
python manage.py create_employees
```

``` bash
# if below commandranwithout anyerrors, 
# it meansyou haveinstalled thisproject successfully.
python manage.py runserver
```
