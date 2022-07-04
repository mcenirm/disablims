def sanitize_phone(value):
    if not value:
        return value
    try:
        return str(sanitize_phone._seed)
    finally:
        sanitize_phone._seed += 1


sanitize_phone._seed = 1_555_555_0000
