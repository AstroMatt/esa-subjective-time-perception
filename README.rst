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
    :email: `stpa@astrotech.io <mailto:stpa@astrotech.io>`_
    :www: `http://www.astromatt.space <http://astromatt.space>`_
    :facebook: `https://facebook.com/astromatt.space <https://facebook.com/astromatt.space>`_
    :linkedin: `https://linkedin.com/in/mattharasymczuk <https://linkedin.com/in/mattharasymczuk>`_
    :slideshare: `https://www.slideshare.net/astrotech/presentations <https://www.slideshare.net/astrotech/presentations>`_


How to use this software?
-------------------------

.. contents::
    :local:

How to run the experiment?
^^^^^^^^^^^^^^^^^^^^^^^^^^

:Device with internet connection:

    1. Run experiment at `stpa.astrotech.io <http://stpa.astrotech.io>`_
    2. Results will be uploaded after each experiment.

:Device without internet connection:

    1. Download https://github.com/AstroMatt/esa-time-perception/archive/master.zip
    2. Extract zip archive.
    3. Copy directory ``frontend/`` (you'll need only this one) to USB disk.
    4. On the other computer copy the directory or run directly from USB disk.
    5. To run, open with your browser ``frontend/index.html`` (double click on this file should be enough).

How to upload results?
^^^^^^^^^^^^^^^^^^^^^^

:Computer can be connected to the internet:

    1. Connect computer to the internet
    2. Open with your browser ``frontend/index.html``.
    3. It should automatically upload results to the internet
    4. Depending on how much experiments was performed, after a minute or so you should be able to see results in the administration panel.

:Computer cannot be connected to the internet:

    1. Open ``frontend/cache.html``
    2. Save all this text as a txt (Notepad or whatever) file to USB Pendrive.
    3. Give me this file (or USB drive), and I will upload this results.
    4. Or send me the results via email: time-perception@haras.pl

How to see results?
^^^^^^^^^^^^^^^^^^^
1. Go to `Administrator Panel <http://stpa.astrotech.io/admin/api_v2/trial/>`_
2. Superuser account is created during instlation of the software please refer to the ``docs/installation.rst``:

    - `Installation <docs/installation.rst>`_
    - `Architecture <docs/architecture.rst>`_
    - `Algorithm <docs/algorithm.rst>`_
    - `API <docs/api.rst>`_
    - `TODO <docs/todo.rst>`_
    - `References <docs/references.rst>`_

