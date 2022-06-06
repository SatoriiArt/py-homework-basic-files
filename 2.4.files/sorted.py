import os

dirname = './sorted'
new_file = 'result.txt'


def file_names(dirname):
    return os.listdir(dirname)


files = file_names(dirname)


def file_lines(file):
    with open(file, 'rt', encoding='utf-8') as f:
        return sum(1 for line in f)


def file_sort(files, dirname):
    file_sizes = dict()
    for file in files:
        size = file_lines(str(dirname) + '/' + str(file))
        if size not in file_sizes:
            file_sizes.update({size: file})
        else:
            file_sizes[size] += file
    file_sorted = dict()
    for i in sorted([i for i in file_sizes.keys()]):
        file_sorted[i] = file_sizes[i]
    return file_sorted


def make_file(file_sorted, dirname, new_file):
    n = open(new_file, 'w')
    for file in file_sorted.keys():
        name = str(file_sorted[file])
        n.write(name + '\n')
        n.write(str(file) + '\n')
        with open(dirname + '/' + name, 'r', encoding='utf-8') as s:
            for line in s:
                n.write(line)
        n.write('\n')
    n.close()


make_file(file_sort(files, dirname), dirname, new_file)
