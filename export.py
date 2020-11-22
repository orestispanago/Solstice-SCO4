import os
import subprocess
from io import StringIO
import pandas as pd
import utils
from setup import check_installation

check_installation()
CWD = os.getcwd()


def raw(direction):
    utils.mkdir_if_not_exists(os.path.dirname(direction.raw_file))
    with open(direction.raw_file, 'w') as f:
        # Solstice cannot take too long string of angle arguments, so split into chunks
        for i in range(0, len(direction.angle_pairs), 50):
            chunk = direction.angle_pairs[i:i + 50]
            chunk = ":".join(chunk)
            cmd = f'solstice -D {chunk} -n {direction.rays} -v -R {direction.receiver} {direction.geometry_path}'.split()
            subprocess.run(cmd, stdout=f)


def df(direction):
    """ Runs Direction and pipes output to dataframe """
    df_list = []
    # Solstice cannot take too long string of angle arguments, so split into chunks
    for i in range(0, len(direction.angle_pairs), 50):
        chunk = direction.angle_pairs[i:i + 50]
        chunk = ":".join(chunk)
        cmd = f'solstice -D {chunk} -n {direction.rays} -v -R {direction.receiver} {direction.geometry_path}'.split()
        a = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        b = StringIO(a.communicate()[0].decode('utf-8'))
        df = pd.read_csv(b, sep='\s+', names=range(47))
        df_list.append(df)
    return pd.concat(df_list)


def vtk(direction, nrays=100000):
    for pair in [direction.angle_pairs[0], direction.angle_pairs[-1]]:
        pair_str = pair.replace(',', '_')
        fname = f"{direction.name}_{pair_str}.vtk"
        utils.mkdir_if_not_exists(direction.shape_dir)
        vtkpath = os.path.join(direction.exp_dir, "shapes", fname)
        cmd = f'solstice  -n {nrays} -p default -t1 -D {pair} -R {direction.receiver} {direction.geometry_path}'.split()
        with open(vtkpath, 'w') as f:
            subprocess.run(cmd, stdout=f)
        utils.del_first_line(vtkpath)


def obj(direction):
    for pair in [direction.angle_pairs[0], direction.angle_pairs[-1]]:
        pair_str = pair.replace(',', '_')
        fname = f"{direction.name}_{pair_str}.obj"
        utils.mkdir_if_not_exists(direction.shape_dir)
        objpath = os.path.join(direction.shape_dir, fname)
        cmd = f'solstice  -n 100 -g format=obj -t1 -D {pair} -R {direction.receiver} {direction.geometry_path}'.split()
        with open(objpath, 'w') as f:
            subprocess.run(cmd, stdout=f)


def heatmap(direction, nrays=1000000):
    receiver_heat = os.path.join(CWD, "geometries", "heatmap", "direction.receiver.yaml")
    geometry_path_heat = os.path.join(CWD, "geometries", "heatmap", "geometry_path.yaml")
    print("WARNING: create a heatmap geometry_path first")
    print("Now using example geometry_path:", geometry_path_heat)
    utils.mkdir_if_not_exists(direction.shape_dir)
    for pair in [direction.angle_pairs[0], direction.angle_pairs[-1]]:
        pair_str = pair.replace(',', '_')
        fname = f"{direction.name}_{pair_str}_heatmap.vtk"
        heat_path = os.path.join(direction.exp_dir, "shapes", fname)
        cmd = f'solstice  -n {nrays} -v -t16 -D {pair} -R {receiver_heat} {geometry_path_heat}'.split()
        with open(heat_path, 'w') as f:
            subprocess.run(cmd, stdout=f)
        utils.del_until(heat_path)
