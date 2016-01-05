# coding: utf-8

from django.db import connection
from django.contrib.humanize.templatetags.humanize import intcomma, intword


def humanize(value):
    try:
        number, word = intword(value).split()
    except AttributeError:
        # lower than 1M
        return intcomma(value, use_l10n=False)
    word = word[0].upper()
    return "%s %s" % (number, word)


def count_estimate(queryset, short=True):
    cursor = connection.cursor()
    cursor.execute("SELECT count_estimate('%s')" % str(queryset.query))
    count = cursor.fetchone()[0]

    if short:
        return humanize(count)
    return count
