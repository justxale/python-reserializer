from .just_helper import check_validity, try_converting_to_list, get_var_type
from .exceptions import InvalidStructureError


# TODO: Optimise this stuff


def decode_jaon(f: str):
    line_number = 0
    namespaces = []  # TODO: Realise this thing
    return_dict = dict()
    first_line_passed = False

    with open(f) as f:
        while line := f.readline().rstrip().removeprefix('\t').removeprefix('    '):
            line_number += 1
            if check_validity(line):  # TODO: Remake line validation with match()
                if line.startswith('data'):
                    buffer = line.removesuffix('>:').split(' <')
                    if len(buffer) < 2:
                        raise InvalidStructureError(f'Invalid structure at line {line_number}: {line}')
                    namespaces = buffer[1].split(', ')

                elif line.startswith('//'):
                    pass  # hm, what should i do with this...

                else:
                    if line.startswith('list') or line.startswith('str'):
                        buffer = line.split(' = ')
                        try_converting_to_list(buffer[1])
                        var_line = buffer[0].split()
                        var_line.append(buffer[1])

                        key = var_line[1]
                        value = get_var_type(var_line[0], var_line[2])

                        return_dict[key] = value

                    else:
                        var_line = line.split()
                        if len(var_line) < 4 or '=' not in var_line:
                            raise InvalidStructureError(f'Invalid structure at line {line_number}: {line}')
                        var_line.remove('=')

                        key = var_line[1]
                        value = get_var_type(var_line[0], var_line[2])
                        return_dict[key] = value
            else:
                raise InvalidStructureError(f'Invalid structure at line {line_number}: {line}')

        # print('Decoding complete with namespaces:', namespaces)
        return return_dict


# TODO: make xml decoder

def decode_xml(f: str):
    return None


# TODO: make xml decoder

def decode_json(f: str):
    return None
