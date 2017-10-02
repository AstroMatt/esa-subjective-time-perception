Plans for further development
=============================

Architectural changes
---------------------
* Implement frontend in `AngularJS 2.0`
* Implement `Django REST framework`

Refactorings
------------
* While API adding:

    - Calculate SHA1 of JSON request
    - Add Result object with JSON request and SHA1
    - Start job of parsing request and converting data to fields
    - Start calculating


* Introduce ``Experiment.clicks_expected`` parameter to make the calculations simpler
* Introduce ``Experiment.clicks_minimum`` parameter to make the calculations simpler
* Introduce ``Experiment.clicks_maximum`` parameter to make the calculations simpler
* Remove ``Trial.regularity``

Functional changes
------------------
* Kiosk mode for single experiments (for Open Day and Conference experiments)
* Create module ``excercise.threadmill`` to store and analyze data from `TomTom Runner Cardio` devices (downloaded from `mysports.tomtom.com <http://mysports.tomtom.com>`_ as `CSV` files)

And much more
-------------
https://github.com/AstroMatt/esa-time-perception/issues