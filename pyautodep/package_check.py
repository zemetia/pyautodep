from pip._internal import main as call_pip
import pkg_resources
from importlib.metadata import packages_distributions
import sys
import re
import requests
import os
import fnmatch


class PyAutoDep:
    def __init__(self, abs_path):
        self.abs_path = abs_path

    def check_package_availability(package: str):
        res = requests.get('https://pypi.org/project/'+package)
        if res.text.find('404'):
            return False
        return True

    def install_package(package: str):
        call_pip(["install", package])

    def install_packages(packages: list[str]):
        not_found: list[str] = list()
        for package in packages:
            if PyAutoDep.check_package_availability(package):
                print("Installing:", package)
                PyAutoDep.install_package(package=package)
            else:
                not_found.append(package)
        if len(not_found) > 0:
            nf = ', '.join(not_found)
            print('the package that can\'t install:', nf)

    def get_path(absolute_path: str, relative_path: str):
        result = os.path.normpath(os.path.join(absolute_path, relative_path))
        return result

    def grab_modules(files: list[str]) -> list[str]:
        modules = set()
        for fname in files:
            file = open(fname,
                        'r').read().split('\n')
            lines = list(set(file[:15]))
            for line in lines:
                if re.match('from', line, re.IGNORECASE):
                    fx = re.sub(r'(?i)from ', '', line)
                    module = re.sub(r'(?i)import ', '', fx)
                elif re.match('import', line, re.IGNORECASE):
                    module = re.sub(r'(?i)import ', '', line)
                else:
                    continue

                if module.count(' ') == 1:
                    cname = module.split(' ')
                    module = cname[0]

                module = module.split('.')[0]
                modules.add(module)
        return modules

    def get_distribution_name(modules: list):
        dist = packages_distributions()
        dists: list[str] = list()
        not_dists: list[str] = list()

        for module in list(modules):
            if module in dist.keys():
                dists.extend(dist[module])
            else:
                not_dists.append(module)

        return set(dists), set(not_dists)

    def check_modules(dists: list[str], not_dists: list[str]):
        buildin_modules: tuple = sys.builtin_module_names

        in_module: list[str] = list()
        in_bi_module: list[str] = list()
        not_module: list[str] = list()

        for pkgd in dists:
            dist: pkg_resources.Distribution = pkg_resources.get_distribution(
                pkgd)
            in_module.append(dist)

        for pkgd in not_dists:
            if pkgd in str(buildin_modules):
                in_bi_module.append(pkgd)
            else:
                not_module.append(pkgd)

        return in_module, in_bi_module, not_module

    def print_info(in_module: list[str], in_bi_module: list[str], not_module: list[str]):
        print("Module's Name : ")
        print("--------------")
        print("[•] Builtin Module [Installed] ")
        for u in in_bi_module:
            print("*. " + u)
        print("\n---------------------")
        print("[•] Installed Module : ")
        for v in in_module:
            print("*.", v)
        print("\n---------------------")
        print("[•] Not Istalled Module : ")
        for w in not_module:
            print("*. " + w)

    def from_file(self, file: str, is_install):
        if len(file) != 0 and fnmatch.fnmatch(file, "*.py"):
            modules = PyAutoDep.grab_modules(
                [PyAutoDep.get_path(self.abs_path, file)])
            dists, not_dists = PyAutoDep.get_distribution_name(modules)
            in_module, in_bi_module, not_module = PyAutoDep.check_modules(
                dists, not_dists)

            PyAutoDep.print_info(in_module, in_bi_module, not_module)

            if is_install:
                print("Installing required modules")
                PyAutoDep.install_packages(not_module)
        else:
            print("input the file path or the file type is not py file ")

    def get_all_py(abs_path):
        file_pattern = '*.py'
        py_files: list[str] = []

        # Loop through all the directories and subdirectories from the root path
        for dirpath, dirnames, filenames in os.walk(abs_path):
            # Loop through all the files in the current directory
            for filename in filenames:
                # Check if the file matches the pattern
                if fnmatch.fnmatch(filename, file_pattern):
                    # If the file matches the pattern, print its absolute path
                    file_path = os.path.join(dirpath, filename)
                    py_files.append(file_path)

        return py_files

    def from_dir(self, dir: str, is_install):
        if len(dir) != 0:
            files = PyAutoDep.get_all_py(
                PyAutoDep.get_path(self.abs_path, dir))
            modules = PyAutoDep.grab_modules(files)
            dists, not_dists = PyAutoDep.get_distribution_name(modules)
            in_module, in_bi_module, not_module = PyAutoDep.check_modules(
                dists, not_dists)

            PyAutoDep.print_info(in_module, in_bi_module, not_module)

        if is_install:
            print("Installing required modules")
            PyAutoDep.install_packages(not_module)
