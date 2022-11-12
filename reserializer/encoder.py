from .just_helper import get_var_type


class ReserializerFile:
    inner_dict = dict()
    var_list = list()
    name = 'unnamed'
    file_format = 'jaon'

    def __init__(self, name: str, file_format: str):
        self.name = name
        self.file_format = file_format

    def add(self, var_type: str, key: str, value):
        self.inner_dict[key] = get_var_type(var_type, str(value))

    def get_dict(self):
        return self.inner_dict

    def encode_data(self):
        return str(self.inner_dict)
        pass

    def export(self):
        with open(f'{self.name}.{self.file_format}', 'w') as f:
            f.writelines(self.encode_data())
