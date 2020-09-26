def del_first_line(fpath):
    # Deletes first line from vtk file to be opened by Paraview
    with open(fpath, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(fpath, 'w') as fout:
        fout.writelines(data[1:])

def del_until(fpath, occurence="# vtk DataFile Version 2.0\n"):
    # Deletes lines from file until occurence of line
    with open(fpath, "r") as fin:
        lines_in = fin.readlines()
    with open(fpath, "w") as fout:
        for count,line in enumerate(lines_in):
            if line == occurence:
                break
        fout.writelines(lines_in[count:])
        
def keep_until(fpath, occurence='reflector', lines_before=0):
    """ Keeps lines until occurence of string """
    with open(fpath, "r") as fin:
        lines_in = fin.readlines()
    with open(fpath, "w") as fout:
        for count,line in enumerate(lines_in):
            if occurence in line:
                break
        fout.writelines(lines_in[:count-lines_before])
