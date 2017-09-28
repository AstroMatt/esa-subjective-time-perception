Subjective Time Perception Analyzer
===================================

How different colors and light polarization influence on time perception?
The software was written for the `Advanced Concepts Team` (`European Space Agency`, `ESTEC`) experiment on subjective time perception.

.. tip:: This software is open source (released under MIT license) and you can use it for your experiments! I would appreciate Pull Requests and any other contribution.

Contact
-------

.. image:: https://travis-ci.org/AstroMatt/esa-time-perception.svg?branch=master
    :target: https://travis-ci.org/AstroMatt/esa-time-perception

- `STPA on SonarCloud <https://sonarcloud.io/dashboard?id=Time-Perception>`_
- `STPA on Github <https://github.com/AstroMatt/esa-time-perception/>`_
- `STPA on Travis CI <https://www.travis-ci.org/AstroMatt/esa-time-perception>`_

**Author**
    :name: `Matt Harasymczuk <http://astromatt.space>`_
    :email: `time-perception@astrotech.io <mailto:time-perception@astrotech.io>`_
    :www: `http://www.astromatt.space <http://astromatt.space>`_
    :facebook: `https://facebook.com/astromatt.space <https://facebook.com/astromatt.space>`_
    :linkedin: `https://linkedin.com/in/mattharasymczuk <https://linkedin.com/in/mattharasymczuk>`_
    :slideshare: `https://www.slideshare.net/astromatt/presentations <https://www.slideshare.net/astromatt/presentations>`_


How to use this software?
-------------------------

.. contents::
    :local:

How to run the experiment?
^^^^^^^^^^^^^^^^^^^^^^^^^^

:Device with internet connection:

    1. Run experiment at http://time.astrotech.io
    2. Results will be uploaded after each experiment.

:Device without internet connection:

    1. Download https://raw.githubusercontent.com/AstroMatt/esa-time-perception/master/frontend/v3/index.html
    2. Oen with your browser ``index.html`` file (double click on this file should be enough).

How to upload results?
^^^^^^^^^^^^^^^^^^^^^^

:Computer can be connected to the internet:

    1. Connect computer to the internet
    2. Oen with your browser ``index.html`` file (double click on this file should be enough).
    3. It should automatically upload results to the internet
    4. Depending on how much experiments was performed, after a minute or so you should be able to see results in the administration panel.

:Computer cannot be connected to the internet:

    1. Download https://github.com/AstroMatt/esa-time-perception/blob/master/frontend/v3/cache.html
    2. Oen with your browser ``cache.html`` file (double click on this file should be enough).
    3. Save all this text as a txt (Notepad or whatever) file to USB Pendrive.
    4. From the other computer send me the results via email: `time-perception@astrotech.io <mailto:time-perception@astrotech.io>`_


How to see results?
^^^^^^^^^^^^^^^^^^^
1. Go to `Administrator Panel <http://time.astrotech.io/admin/api_v2/trial/>`_
2. Superuser account is created during instlation of the software please refer to the ``docs/installation.rst``:

    - `Installation <docs/installation.rst>`_
    - `Architecture <docs/architecture.rst>`_
    - `Algorithm <docs/algorithm.rst>`_
    - `API <docs/api.rst>`_
    - `TODO <docs/todo.rst>`_
    - `References <docs/references.rst>`_

