django-psql-estimate
======================

Estimate expensive COUNTs in Django/Postgres.

Quick howto
-----------

.. code-block:: python

    import psql_estimate
    qs = SomeModel.objects.filter(title="Foo")
    psql_estimate.count_estimate(qs)
