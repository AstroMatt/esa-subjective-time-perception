Plans for further development
=============================

Architectural changes
---------------------
* Implement frontend in `AngularJS 2.0`
* Implement `Django REST framework`

Refactorings
------------
* Introduce ``Trial.expected_clicks`` parameter to make the calculations simpler
* Remove ``Trial.regularity``
* Rename ``Trial.time_mean_*`` to ``Trial.interval_*``
* Rename ``Trial.time_stdev_*`` to ``Trial.regularity_*``
* Rename ``Trial.percentage_*`` to ``Trial.tempo_*``

Functional changes
------------------
* Create experiment creation wizard
* Serve experiment setup as ``json`` file to the browser
* Support running multiple different offline experiments
* Kiosk mode for single experiments (for Open Day and Conference experiments)
* Create reports page with graphical data analysis
* Create module ``excercise.threadmill`` to store and analyze data from `TomTom Runner Cardio` devices (downloaded from `mysports.tomtom.com <http://mysports.tomtom.com>`_ as `CSV` files)
* Write time guessing mini-game
