def divider(a, b):
    if not a or not b:
        raise ValueError("Empty")

    elif a < b:
        raise ValueError("a < b")

    elif b > 100:
        raise IndexError("b > 100")

    return a / b


data_list = [[None, None], [10, 2], [2, 5], ["123", 4], [18, 0], [[], 15], [8, 4]]
data = {}
for key, value in data_list:
    if key and value:
        try:
            data[key] = value
        except Exception as error:
            print(f"{type(error).__name__}: {error}")  # noqa
print(data)
result = []

# result = [divider(key, data[key]) for key in data]

for key in data:
    try:
        result.append(divider(key, data[key]))

    except Exception as error:
        print(f"{type(error).__name__}: {error}")  # noqa

print(result)
