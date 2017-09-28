Subjective Time Perception Analyzer
===================================

How different colors and light polarization influence on time perception?
The software was written for the `Advanced Concepts Team` (`European Space Agency`, `ESTEC`) experiment on subjective time perception.

.. tip:: This software is open source (released under MIT license) and you can use it for your experiments! I would appreciate Pull Requests and any other contribution.


Running the experiment online via http://time.astrotech.io
----------------------------------------------------------
1. Run experiment at http://time.astrotech.io
2. Results will be uploaded after each experiment.


Running the experiment offline (device without access to the internet)
----------------------------------------------------------------------
1. Download https://raw.githubusercontent.com/AstroMatt/esa-time-perception/master/frontend/v3/index.html
2. Open with your browser (double click) ``index.html`` file and run the experiment.
3. When you connect machine to the internet, refresh page and your results will be uploaded.
4. If your computer cannot be connected to the internet:

    1. Download https://github.com/AstroMatt/esa-time-perception/blob/master/frontend/v3/cache.html
    2. Open with your browser (double click) ``cache.html`` file.
    3. Save all this text as a txt (in Notepad, Word or whatever else) file to USB Pendrive.
    4. From the other computer send the results via email: `time-perception@astrotech.io <mailto:time-perception@astrotech.io>`_


How to see results?
-------------------
1. Go to `Administrator Panel <http://time.astrotech.io/admin/api_v2/trial/>`_
2. Superuser account is created during instlation of the software please refer to the ``docs/installation.rst``:

    - `Installation <docs/installation.rst>`_
    - `Architecture <docs/architecture.rst>`_
    - `Algorithm <docs/algorithm.rst>`_
    - `TODO <docs/todo.rst>`_
    - `References <docs/references.rst>`_


Development - CI/CD
-------------------
- `API <docs/api.rst>`_

.. image:: https://travis-ci.org/AstroMatt/esa-time-perception.svg?branch=master
    :target: https://travis-ci.org/AstroMatt/esa-time-perception

- `STPA on SonarCloud <https://sonarcloud.io/dashboard?id=Time-Perception>`_
- `STPA on Github <https://github.com/AstroMatt/esa-time-perception/>`_
- `STPA on Travis CI <https://www.travis-ci.org/AstroMatt/esa-time-perception>`_

Contact
-------

:name: `Matt Harasymczuk <http://astromatt.space>`_
:email: `time-perception@astrotech.io <mailto:time-perception@astrotech.io>`_
:www: `http://www.astromatt.space <http://astromatt.space>`_
:facebook: `https://facebook.com/astromatt.space <https://facebook.com/astromatt.space>`_
:linkedin: `https://linkedin.com/in/mattharasymczuk <https://linkedin.com/in/mattharasymczuk>`_
:slideshare: `https://www.slideshare.net/astromatt/presentations <https://www.slideshare.net/astromatt/presentations>`_
