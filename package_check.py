from pip._internal import main as call_pip
from pip._internal.operations import freeze
import pkg_resources
from importlib.metadata import packages_distributions
import sys
import re
import numpy
import pandas
import cv2
import requests


def check_package_availability(package: str):
    res = requests.get('https://pypi.org/project/'+package)
    if res.text.find('404'):
        return False
    return True


def install_package(package):
    call_pip(["install", package])


def grab_modules(files: list[str]) -> list[str]:
    modules = set()
    for fname in files:
        file = open(fname, 'r').read().split('\n')
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


args = sys.argv
args.pop(0)

if len(args) != 0:
    modules = grab_modules(args)
    dists, not_dists = get_distribution_name(modules)
    in_module, in_bi_module, not_module = check_modules(dists, not_dists)

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

    for i in not_module:
        print(i, check_package_availability(i))

else:
    print('Give the argument..')
    print(
        '~ python reqpip.py [Your Python Filename] [Another Python Filename] [Another Python Filename] [...]\n')
    print('For example : ')
    print('~ python reqpip.py --file test.py hello.py')
    print('~ python reqpip.py --dir .')
