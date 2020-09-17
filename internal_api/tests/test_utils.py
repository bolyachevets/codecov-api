def to_drf_datetime_str(datetime):
    """
    DRF does custom datetime representation, which makes comparing
    expected timestamps in tests really annoying. This function tries
    to mimic DRF datetime representation using ISO-8601 format, minus
    reading from gobal formatting settings.

    source: https://github.com/encode/django-rest-framework/blob/aed74961ba03e3e6f53c468353f4e255eb788555/rest_framework/fields.py#L1227
    """
    value = datetime.isoformat()
    if value.endswith('+00:00'):
        value = value[:-6] + 'Z'
    return value