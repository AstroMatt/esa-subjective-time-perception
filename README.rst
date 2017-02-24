Subjective Time Perception Analyzer
===================================

How different colors and light polarization influence on time perception?

The software was written for the `Advanced Concepts Team` (`European Space Agency`, `ESTEC`) experiment on subjective time perception.

It is open source (released under MIT license) and you can use it for your experiments!

How to use this software?
-------------------------

How to run the experiment?
^^^^^^^^^^^^^^^^^^^^^^^^^^
When computer has internet connection:

1. Run experiment on `stpa.astrotech.io <http://stpa.astrotech.io>`_
2. Results will be uploaded after each experiment.

When experiment need to work offline (on computer without internet connection):

1. Download https://github.com/AstroMatt/esa-time-perception/archive/master.zip
2. Extract zip archive.
3. Copy directory ``frontend/`` (you'll need only this one) to USB disk.
4. On the other computer copy the directory or run directly from USB disk.
5. To run, open with your browser ``frontend/index.html`` (double click on this file should be enough).

How to upload results?
^^^^^^^^^^^^^^^^^^^^^^
Computer can be connected to the internet:

1. Connect computer to the internet
2. Open with your browser ``frontend/index.html``.
3. It should automatically upload results to the internet
4. Depending on how much experiments was performed, after a minute or so you should be able to see results in the administration panel.

Computer can not be connected to the internet:

1. Open ``frontend/cache.html``
2. Save all this text as a txt (Notepad or whatever) file to USB Pendrive.
3. Give me this file (or USB drive), and I will upload this results.
4. Or send me the results via email: time-perception@haras.pl

How to see results?
^^^^^^^^^^^^^^^^^^^
1. Go to `Trial Administrator Panel <http://stpa.astrotech.io/admin/api_v2/trial/>`_
2. You should know login and password :)

.. toctree::
    :maxdepth: 2
    :numbered:
    :caption: Table of Contents
    :glob:

    docs/about.rst
    docs/usage.rst
    docs/architecture.rst
    docs/algorithm.rst
    docs/data.rst
    docs/api.rst
    docs/todo.rst
