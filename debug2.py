def divider(a, b):
    if a < b:
        raise ValueError

    elif b > 100:
        raise IndexError

    return a / b


try:
    data = {None: None, 10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
except Exception as error:
    print(f"{type(error).__name__}: {error}")  # noqa

try:
    result = [divider(key, data[key]) for key in data]

except Exception as error:
    print(f"{type(error).__name__}: {error}")  # noqa

else:
    print(result)
