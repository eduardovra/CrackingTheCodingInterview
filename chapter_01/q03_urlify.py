
def urlify(url: str, size: int) -> str:
    array: list = []

    for i in range(size):
        c = url[i]
        if c == ' ':
            array.extend('%20')
        else:
            array.append(c)

    return ''.join(array)

assert urlify("Mr John Smith      ", 13) == "Mr%20John%20Smith"
