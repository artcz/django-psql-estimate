# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

import os.path


class RunSQLFile(migrations.RunSQL):
    """
    Source: https://github.com/mrzechonek/sql_condemned
    """

    def __init__(self, filename):
        directory = os.path.dirname(os.path.realpath(filename))

        basename, _ = os.path.splitext(os.path.basename(filename))

        with open(os.path.join(directory, basename)) as sql_file:
            super(RunSQLFile, self).__init__(sql_file.read())


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        RunSQLFile("create_count_estimate_function.sql")
    ]
