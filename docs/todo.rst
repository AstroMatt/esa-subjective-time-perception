Plans for further development
=============================

Architectural changes
---------------------
* Implement `Django REST framework`

Refactorings
------------
* While API adding:

    - Add field status instead of verified: None, Added, Parsed, Error, Valid, Invalid
    - Calculate JSON's SHA1 from incoming HTTP request body
    - Add Result object to Database with JSON request and SHA1 (no other fields), set status Added
    - Start job of parsing request and converting data to fields, on finish change status (Parsed or Error)
    - Start calculating data, on finish change status (Valid, Invalid)

.. code-block:: python


    STATUS_ADDED = 'added'
    STATUS_PARSED = 'parsed'
    STATUS_ERROR = 'error'
    STATUS_VALID = 'valid'
    STATUS_INVALID = 'invalid'
    STATUS_RECALCULATE = 'recalculate'
    STATUS_CHOICES = [
        (STATUS_ADDED, _('Added')),
        (STATUS_PARSED, _('Parsed')),
        (STATUS_ERROR, _('Error')),
        (STATUS_VALID, _('Valid')),
        (STATUS_INVALID, _('Invalid')),
        (STATUS_RECALCULATE, _('To Recalculate'))]

    request_data = models.TextField(verbose_name=_('HTTP Request JSON'), null=True, blank=True, default=None)
    request_sha1 = models.CharField(verbose_name=_('HTTP Request SHA1'), max_length=40, db_index=True, unique=True)
    status = models.CharField(verbose_name=_('Status'), max_length=30, choices=STATUS_CHOICES, default=STATUS_ADDED)



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