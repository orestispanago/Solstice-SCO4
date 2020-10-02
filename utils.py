def del_first_line(fpath):
    # Deletes first line from vtk file to be opened by Paraview
    with open(fpath, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(fpath, 'w') as fout:
        fout.writelines(data[1:])

def del_until(fpath, occurrence="# vtk DataFile Version 2.0\n"):
    # Deletes lines from file until occurence of line
    with open(fpath, "r") as fin:
        lines_in = fin.readlines()
    with open(fpath, "w") as fout:
        for count,line in enumerate(lines_in):
            if line == occurrence:
                break
        fout.writelines(lines_in[count:])
        
def keep_until(fpath, occurrence='reflector', lines_before=0):
    """ Keeps lines until occurrence of string """
    with open(fpath, "r") as fin:
        lines_in = fin.readlines()
    with open(fpath, "w") as fout:
        for count,line in enumerate(lines_in):
            if occurrence in line:
                break
        fout.writelines(lines_in[:count-lines_before])

def replace_line(fpath, occurence="&absorber_translation", newline=""):
    """ Replaces line that contains occurrence with new line """
    with open(fpath, "r") as fin:
        lines_in = fin.readlines()
    with open(fpath, "w") as fout:
        for count,line in enumerate(lines_in):
            if occurence in line:
                break
        lines_in[count] = newline
        fout.writelines(lines_in)



    