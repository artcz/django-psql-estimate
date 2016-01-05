django-psql-estimate
======================

Estimate expensive COUNTs in Django/Postgres.

https://pypi.python.org/pypi/django-psql-estimate

Quick howto
-----------

pip install django-psql-estimate, then

.. code-block:: python

    import psql_estimate
    qs = SomeModel.objects.filter(title="Foo")
    psql_estimate.count_estimate(qs)
