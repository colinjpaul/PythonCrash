def read_files(filename):
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_files(filename)
