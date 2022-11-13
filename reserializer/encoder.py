from .just_helper import get_var_type


class ReserializerFile:
    """
    Class representating the File user creates via :py:meth:`reserializer.create()`
    """
    inner_dict = dict()
    var_list = list()
    name = 'unnamed'
    file_format = 'jaon'

    def __init__(self, name: str, file_format: str):
        self.name = name
        self.file_format = file_format

    def add_field(self, var_type: str, key: str, value):
        """
        Adds a field to file
        :param var_type: var type you want to add
        :param key: key for this value
        :param value: value for key
        """
        buffer = get_var_type(var_type, str(value))

        if "'" in value:
            buffer = ('"' + buffer + '"')
        else:
            buffer = ("'" + buffer + "'")
        self.inner_dict[key] = buffer
        self.var_list.append([var_type, key])

    def get_values(self):
        """
        Returns a Dictionary
        :return: dict() with stored data
        """
        return self.inner_dict

    def get_value(self, key):
        try:
            return self.inner_dict[key]
        except KeyError:
            print(f"{key} wasn't found")
            return None

    def export(self):
        """
        Exports ReserializerFile to file
        """
        lines_list = list()
        buffer_var_list = self.var_list.copy()
        with open(f'{self.name}.{self.file_format}', 'w') as f:
            lines_list.append(f'data {self.file_format} {self.name} <1.0>:\n')
            # print('Encoding...')
            while buffer_var_list:
                # print('Processing', buffer_var_list[0])
                lines_list.append(f'\t{buffer_var_list[0][0]} {buffer_var_list[0][1]} = '
                                  f'{str(self.inner_dict[buffer_var_list[0][1]])}\n')
                del buffer_var_list[0]
            f.writelines(lines_list)


class JAONFile:
    def __init__(self):
        pass

    def export(self):
        pass
