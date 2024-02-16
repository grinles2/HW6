result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b

while True:
    try:
        data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
    for key in data:
        res = divider(key, data[123])
        result.append(res)
print(result)
    except TypeError as te:
        data = {10: 2, 2: 5, "123": 4, 18: 0, [None]: 15, 8: 4}
    for key in data:
        res = divider(key, data[123])
        result.append(res)
print(result)
    except SyntaxError as se:
        data = {10: 2, 2: 5, "123": 4, 18: 0, [None]: 15, 8: 4}
    for key in data:
        res = divider(key, data[123])
        result.append(res)
print(result)
    else:
        print("ELSE")
    finally:
        print("FINALLY")
