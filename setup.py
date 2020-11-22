import requests
import zipfile
import io
import tarfile
import urllib.request
import os
from subprocess import check_output

base_url = "https://www.meso-star.com/projects/solstice/downloads/"
folder = "solstice"


class Platform:

    def set_paths(self):
        print("Setting up paths...", end='')
        os.environ["LD_LIBRARY_PATH"] = os.path.join(self.solstice_path, "lib")
        os.environ["MANPATH"] = os.path.join(self.solstice_path, 'share', 'man')
        os.environ["PATH"] += os.path.join(self.solstice_path, "bin")
        print("OK")

    def found_solstice(self):
        install_dir = os.path.join(os.getcwd(), folder, self.dirname)
        if os.path.exists(install_dir) and len(os.listdir(install_dir)) != 0:
            print("Found solstice in", install_dir)
            return True
        print("Solstice not found")
        return False

    def solstice_path_ok(self):
        if self.solstice_path in os.environ["PATH"]:
            print("Path ok, using ", self.solstice_path)
            return True
        return False


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
        print("Extracting...", end="")
        tar.extractall(folder)
        print("OK")
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


def check_installation():
    platform = init_platform()
    if platform.found_solstice():
        if platform.solstice_path_ok():
            try:
                solstice_works()
            except FileNotFoundError:
                print("tried solstice -h, no luck")
                platform.set_paths()
        else:
            platform.set_paths()
    else:
        platform.download_extract()
        platform.set_paths()


check_installation()
