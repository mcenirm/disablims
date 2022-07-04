"overly simplistic sanitizers that just increment with each use"

import dataclasses


@dataclasses.dataclass(kw_only=True)
class CountingSanitizer:
    seed: int = 0
    fmt: str = "{0}"
    __doc__: str | None = None

    def __call__(self, value):
        if not value:
            return value
        try:
            return self.fmt.format(self.seed)
        finally:
            self.seed += 1


_sanitizers = {}


def __getattr__(name: str):
    if name.startswith("sanitize_"):
        prefix = "".join(w[0] for w in name.removeprefix("sanitize_").split("_"))
        s = _sanitizers.get(name)
        if s is None:
            s = CountingSanitizer(fmt=prefix + "{0}")
            _sanitizers[name] = s
        return s
    raise AttributeError(f"module {__name__} has no attribute {name}")


sanitize_phone = CountingSanitizer(seed=1_555_555_0000)
sanitize_email = CountingSanitizer(fmt="em{0}@x{0}.sanitized.net")
sanitize_given_name = CountingSanitizer(fmt="gn{0}")
sanitize_surname = CountingSanitizer(fmt="sn{0}")
sanitize_username = CountingSanitizer(fmt="un{0}")
sanitize_test_item = __getattr__("sanitize_test_item")


def test_phone():
    """
    phone number
    >>> sanitize_phone(None)
    >>> sanitize_phone("1234567890")
    '15555550000'
    >>> sanitize_phone(1928374650)
    '15555550001'
    >>>"""


def test_email():
    """email address
    >>> sanitize_email(None)
    >>> sanitize_email("jdoe@example.com")
    'em0@x0.sanitized.net'
    >>> sanitize_email("jdoe@example.com")
    'em1@x1.sanitized.net'
    >>>
    """


def test_given_name():
    """given name
    >>> sanitize_given_name(None)
    >>> sanitize_given_name("John")
    'gn0'
    >>> sanitize_given_name("John")
    'gn1'
    >>>
    """


def test_surname():
    """surname
    >>> sanitize_surname(None)
    >>> sanitize_surname("John")
    'sn0'
    >>> sanitize_surname("John")
    'sn1'
    >>>
    """


def test_username():
    """username
    >>> sanitize_username(None)
    >>> sanitize_username("jdoe")
    'un0'
    >>> sanitize_username("jdoe")
    'un1'
    >>>
    """


def test_test_item():
    """test item
    >>> sanitize_test_item(None)
    >>> sanitize_test_item("test")
    'ti0'
    >>> sanitize_test_item("test")
    'ti1'
    """
