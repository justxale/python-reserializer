import reserializer

output_file = reserializer.ReserializerFile('test_output', 'jaon')
for i in range(1, 100_000):
    output_file.add_field('str', 'cool_str' + str(i), "stuff for funkin'")
output_file.export()

print(reserializer.load('test_output.jaon'))
