def sanitize_empty_array(value):
    """empty serialized PHP array
    >>> sanitize_empty_array(None)
    >>> sanitize_empty_array('a:1:{s:3:"foo";s:3:"bar";}')
    'a:0:{}'
    >>>
    """
    if not value:
        return value
    return "a:0:{}"
