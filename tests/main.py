import reserializer

print(reserializer.load('test.jaon'))

output_file = reserializer.ReserializerFile('test_output', 'jaon')
output_file.add('list', 'cool_list', [1, 3, 5])
output_file.export()