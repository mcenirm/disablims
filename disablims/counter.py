"overly simplistic sanitizers that just increment with each use"


def sanitize_phone(value):
    """phone number
    >>> sanitize_phone(None)
    >>> sanitize_phone("1234567890")
    '15555550000'
    >>> sanitize_phone(1928374650)
    '15555550001'
    >>>
    """
    if not value:
        return value
    try:
        return str(sanitize_phone._seed)
    finally:
        sanitize_phone._seed += 1


def sanitize_email(value):
    """email address
    >>> sanitize_email(None)
    >>> sanitize_email("jdoe@example.com")
    'em0@x0.sanitized.net'
    >>> sanitize_email("jdoe@example.com")
    'em1@x1.sanitized.net'
    >>>
    """
    if not value:
        return value
    try:
        return "em{0}@x{0}.sanitized.net".format(sanitize_email._seed)
    finally:
        sanitize_email._seed += 1


def sanitize_given_name(value):
    """given name
    >>> sanitize_given_name(None)
    >>> sanitize_given_name("John")
    'gn0'
    >>> sanitize_given_name("John")
    'gn1'
    >>>
    """
    if not value:
        return value
    try:
        return "gn{0}".format(sanitize_given_name._seed)
    finally:
        sanitize_given_name._seed += 1


def sanitize_surname(value):
    """surname
    >>> sanitize_surname(None)
    >>> sanitize_surname("John")
    'sn0'
    >>> sanitize_surname("John")
    'sn1'
    >>>
    """
    if not value:
        return value
    try:
        return "sn{0}".format(sanitize_surname._seed)
    finally:
        sanitize_surname._seed += 1


sanitize_phone._seed = 1_555_555_0000
sanitize_email._seed = 0
sanitize_given_name._seed = 0
sanitize_surname._seed = 0
