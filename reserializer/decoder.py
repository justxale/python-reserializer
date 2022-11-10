import re
from typing import IO


def decode(f: str):
    with open(f, 'r') as f:
        data = list()
        group = dict()
        for key, value in re.findall(r'(.*):\s*([\dE+-.]+)', f.read()):
            if key in group:
                data.append(group)
                group = dict()
            group[key] = value
        data.append(group)

    print(data)


class ReserializerDecoder:
    value = None

    def __init__(self):
        pass
