django-suc
==========

**django-suc** spares you from manually assigning a unique name to a constraint

Installation
------------

You can install **django-suc** by using pip::

    $ pip install django-suc

Quickstart
----------

In your apps.py:

.. code-block:: python

    from django_suc import SmartAppConfig

    class MyAppConfig(SmartAppConfig):
        ...


In your models.py:

.. code-block:: python

    from django.db import models
    from django_suc import SmartUniqueConstraint

    class MyClass(models.Model):
        ...
        class Meta:
            constraints = [
                SmartUniqueConstraint(fields=['field1', 'field2']),
            ]
