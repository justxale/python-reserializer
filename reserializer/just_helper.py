from ast import literal_eval


def check_validity(line: str) -> bool:
    if not line.startswith('    ') and (
            line.startswith('data') or
            line.startswith('int') or
            line.startswith('float') or
            line.startswith('str') or
            line.startswith('bool') or
            line.startswith('list') or
            line.startswith('var') or
            line.startswith('//') or
            line.startswith('/*') or
            line.startswith('*/')
    ):
        return True
    else:
        return False


def get_var_type(var: str, value: str):
    match var:
        case 'str':
            try:
                value = value.removeprefix('"').removeprefix("'").removesuffix('"').removesuffix("'")
                return str(value)
            except ValueError:
                print('Cannot be processed. Passing...')
        case 'int':
            try:
                return int(value)
            except ValueError:
                print('Cannot be processed. Passing...')
        case 'float':
            try:
                return float(value)
            except ValueError:
                print('Cannot be processed. Passing...')
        case 'list':
            try:
                return value
            except ValueError:
                print('Cannot be processed. Passing...')


def try_converting_to_list(value: str):
    if value.startswith('[') and value.endswith(']'):
        buffer = literal_eval(value)
        return buffer
    else:
        print('Passing', value)
        return value
