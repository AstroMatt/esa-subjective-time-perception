Technology and Architecture
===========================
`Subjective Time Perception Analyzer` (`STPA`) is written as a web application platform. It uses frontend/backend model. Frontend is written in JavaScript with `jQuery` library to handle AJAX requests. Backend is written in `Python` using `Django` framework. Application was ment to be used both online and offline.

Layers
------

Backend
^^^^^^^


Frontend
^^^^^^^^


Using the application
---------------------

Offline usage
^^^^^^^^^^^^^
Application starts in offline mode and allow user to run the experiment on the local device. Synchronization procedure is described in `Uploading experiment results to database`_.

Online usage
^^^^^^^^^^^^
Application is working by default in online mode.  After the experiment results are stored in database and synchronized with the remote server. Synchronization procedure is described in `Uploading experiment results to database`_.

Uploading experiment results to database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Results are stored in web-browser ``localStorage``. Each time when application is on the main screen or after the experiment it makes the ``HEAD /api/v2/ HTTP/1.1`` request to the server to check whether server responds and is available for receiving results. If server is accepting results then the results will be pushed and upon successful synchronization the ``localStorage`` cache will be cleared.

In case of device being permanently unable to connect to the internet application allows to fetch the cache data by accessing ``/cache.html`` address. Displayed content is a JSON representation of ``localStorage`` data collected by application and not yet uploaded to the remote database.

The application is also immune to uploading the same results once again (eg. in case of connecting device to the internet, from which cache was manually copied before). It will not double the results in database on synchronization but clear the local computer cache.
