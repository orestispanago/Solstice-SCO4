import requests
import zipfile
import io
import tarfile
import urllib.request
import os
from subprocess import check_output

base_url = "https://www.meso-star.com/projects/solstice/downloads/"
folder = "solstice"


class Platform():
    def __init__(self):
        pass

    def set_paths(self):
        print("setting up paths...")
        os.environ["LD_LIBRARY_PATH"] = os.path.join(self.solstice_path, "lib")
        os.environ["MANPATH"] = os.path.join(self.solstice_path, 'share', 'man')
        if "solstice" not in os.environ["PATH"]:
            os.environ["PATH"] += os.path.join(self.solstice_path, "bin")


class Windows(Platform):
    def __init__(self):
        super().__init__()
        self.dirname = "Solstice-0.9.0-Win64"
        self.url = base_url + self.dirname + ".zip"
        self.solstice_path = ";" + os.path.join(os.getcwd(), folder, self.dirname)

    def download_extract(self):
        """ Downloads and extracts zip file to specified folder"""
        print("Downloading " + self.dirname + "...")
        r = requests.get(self.url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        print("Extracting...")
        z.extractall(folder)
        return self


class Linux(Platform):
    def __init__(self):
        super().__init__()
        self.dirname = "Solstice-0.9.0-GNU-Linux64"
        self.url = base_url + self.dirname + ".tar.gz"
        self.solstice_path = ":" + os.path.join(os.getcwd(), folder, self.dirname)

    def download_extract(self):
        print("Downloading " + self.dirname + "...")
        req = urllib.request.urlretrieve(self.url, filename=None)[0]
        tar = tarfile.open(req)
        print("Extracting...")
        tar.extractall(folder)
        return self


def init_platform():
    if os.name == "nt":
        return Windows()
    else:
        return Linux()


def solstice_works():
    cmd = "solstice -h".split()
    process = check_output(cmd)
    if "Usage" in process.decode("utf-8"):
        return True
    return False


def install():
    init_platform().download_extract().set_paths()
    if solstice_works():
        print("installation successful!")


if __name__ == "main":
    init_platform().set_paths()

    if not os.path.exists(folder) or len(os.listdir(folder)) == 0:
        print("solstice not found in project, installing...")
        install()
    if not solstice_works():
        install()
    else:
        print("solstice is installed and works!")
