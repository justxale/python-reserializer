import reserializer

output_file = reserializer.ReserializerFile('test_output', 'jaon')
for i in range(1, 100):
    output_file.add_field('str', 'cool_str' + str(i), "stuff for funkin'")
output_file.export()
print(output_file.get_value('test'))

print(reserializer.load('test_output.jaon'))
