Installation
============

.. code-block:: sh

    git clone https://github.com/AstroMatt/esa-time-perception.git
    cd esa-time-perception
    python3 -m vevn virtualenv
    source virtualenv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

    open http://localhost:8000/
    open http://localhost:8000/admin/



