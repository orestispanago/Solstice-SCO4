import os


def mkdir_if_not_exists(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def read_lines(fpath):
    with open(fpath, 'r') as fin:
        lines = fin.readlines()
    return lines


def del_first_line(fpath):
    """ Deletes first line from vtk file to be opened by Paraview """
    lines = read_lines(fpath)
    with open(fpath, 'w') as fout:
        fout.writelines(lines[1:])


def del_until(fpath, occurrence="# vtk DataFile Version 2.0\n"):
    """ Deletes lines from file until occurrence of line """
    lines_in = read_lines(fpath)
    with open(fpath, "w") as fout:
        for count, line in enumerate(lines_in):
            if line == occurrence:
                break
        fout.writelines(lines_in[count:])


def keep_until(fpath, occurrence='reflector', lines_before=0):
    """ Keeps lines until occurrence of string """
    lines_in = read_lines(fpath)
    with open(fpath, "w") as fout:
        for count, line in enumerate(lines_in):
            if occurrence in line:
                break
        fout.writelines(lines_in[:count - lines_before])


def replace_line(fpath, occurrence="&abs_x", newline=""):
    """ Replaces line that contains occurrence with new line """
    lines_in = read_lines(fpath)
    with open(fpath, "w") as fout:
        for count, line in enumerate(lines_in):
            if occurrence in line:
                break
        lines_in[count] = newline
        fout.writelines(lines_in)


def replace_occurence_and_four_next(fpath, occurrence="", newlines=""):
    """ Replaces line containing occurence and next four with newlines """
    lines_in = read_lines(fpath)
    with open(fpath, "w") as fout:
        for count, line in enumerate(lines_in):
            if occurrence in line:
                break
        lines_in[count:count + 5] = newlines
        fout.writelines(lines_in)
