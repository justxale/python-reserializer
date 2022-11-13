import gc

from .just_helper import get_var_type


class ReserializerFile:
    inner_dict = dict()
    var_list = list()
    name = 'unnamed'
    file_format = 'jaon'

    def __init__(self, name: str, file_format: str):
        self.name = name
        self.file_format = file_format

    def add_field(self, var_type: str, key: str, value):
        buffer = get_var_type(var_type, str(value))

        print(str(value))
        print('after get_var_type():', buffer)

        if "'" in value:
            buffer = ('"' + buffer + '"')
        else:
            buffer = ("'" + buffer + "'")
        print(buffer)
        self.inner_dict[key] = buffer
        self.var_list.append([var_type, key])

    def get_dict(self):
        return self.inner_dict

    def export(self, optimised: bool = False):
        lines_list = list()
        buffer_var_list = self.var_list.copy()
        with open(f'{self.name}.{self.file_format}', 'w') as f:
            lines_list.append(f'data {self.file_format} {self.name} <1.0>:\n')
            print('Encoding...')
            while buffer_var_list:
                print('Processing', buffer_var_list[0])
                lines_list.append(f'\t{buffer_var_list[0][0]} {buffer_var_list[0][1]} = '
                                  f'{str(self.inner_dict[buffer_var_list[0][1]])}\n')

                # del self.inner_dict[self.var_list[0][1]] # We don't delete class dict cuz user may need it later
                del buffer_var_list[0]

            if not optimised:
                f.writelines(lines_list)


class JAONFile:
    def __init__(self):
        pass

    def export(self):
        pass
