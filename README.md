django-cms
==========
create virtual environment 
https://github.com/vinodpandey/blog/blob/master/virtualenv-python2.7.3.sh
cd virtual-env-dir
git clone git@github.com:vinodpandey/django-cms.git project
source bin/activate

install requirements
pip install -r requirements.txt

Create a 'secrets.json' file in the directoy above the checkout, containing
   something like::

    { "secret_key": "xyz",
      "superfeedr_creds": ["any@email.com", "some_string"] }

Basic steps:
https://github.com/django/djangoproject.com




