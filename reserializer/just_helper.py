from ast import literal_eval


def check_validity(line: str) -> bool:
    if not line.startswith('\t') and (
            line.startswith('data') or
            line.startswith('int') or
            line.startswith('float') or
            line.startswith('str') or
            line.startswith('bool') or
            line.startswith('list') or
            line.startswith('var') or
            line.startswith('//')  # or
            # line.startswith('/*') or
            # line.startswith('*/') # TODO: Multiline structure???
    ):
        return True
    else:
        return False


def get_var_type(var: str, value: str, encoding: bool = False):
    print('??', value)
    match var:
        case 'bool' | 'list':
            try:
                return literal_eval(value)
            except ValueError:
                print(value, 'cannot be processed. Passing...')
                pass
        case 'str':
            try:
                if encoding:
                    return str(value)
                else:
                    return str(value.removeprefix('"').removeprefix("'").removesuffix('"').removesuffix('"'))
            except ValueError:
                print(value, 'cannot be processed. Passing...')
            pass
        case 'int':
            try:
                return int(float(value))
            except ValueError:

                print(value, 'cannot be processed. Passing...')
                pass
        case 'float':
            try:

                return float(value)
            except ValueError:

                print(value, 'cannot be processed. Passing...')
                pass
        case _:
            print('Unrecognised var type')
            pass


def try_converting_to_list(value: str):
    if value.startswith('[') and value.endswith(']'):
        buffer = literal_eval(value)
        return buffer
    else:
        # print('Passing', value)
        return value
