def func(num):
    try:
        return int(num)*2
    except (ValueError, TypeError) as err:
        return err
