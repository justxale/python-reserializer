import re
from typing import IO


# TODO: Develop new Decode method
def decode(f: str):
    file_lines = None
    buffer = []
    data = {}
    with open(f, 'r') as f:
        file_lines = f.readlines()
    for i in file_lines:
        buffer.append(i.replace('    ', '').replace('\n', ''))
    return data


class ReserializerDecoder:
    value = None

    def __init__(self):
        pass
