from typing import Any


def divider(a: float | int, b: float | int) -> float:
    if not a or not b:
        raise ValueError("Empty")
    elif type(a) == str:
        a = int(a)


    elif a < b:
        raise ValueError("a < b")

    elif b > 100:
        raise IndexError("b > 100")

    return a / b


def convert_to_dict(inp: list[Any, Any]) -> dict:
    data = {}
    for key, value in inp:
        if key and value:
            try:
                data[key] = value
            except Exception as error:
                print(f"{type(error).__name__}: {error}")  # noqa
    return data


def process(inp: dict) -> list:
    # result = [divider(key, data[key]) for key in data]
    result = []
    for key in inp:
        try:
            result.append(divider(key, data[key]))

        except Exception as error:
            print(f"{type(error).__name__}: {error}")  # noqa
    return result


if __name__ == "__main__":
    data = convert_to_dict([[None, None], [10, 2], [2, 5], ["123", 4], [18, 0], [[], 15], [8, 4]])
    print(data)

    result = process(data)
    print(result)
