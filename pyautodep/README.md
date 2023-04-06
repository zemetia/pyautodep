# PyAutoDep

an auto installer module to install all imported library python on your project (Development)

## How to Install

Install the `pyautodep` package with pip

```
pip install pyautodep
```

## How to Use

```
python -m pyautodep -t file -p [file_name].py
```

```
python -m pyautodep -t folder -p .
```

Add `-i` or `--install` to install all missing modules founded

```
python -m pyautodep -t folder -p . -i
```

```
python -m pyautodep -t folder -p . --install
```

## Output Example

```
Module's Name :
--------------
[•] Builtin Module [Installed]
*.
*. re
*. codecs
*. sys

---------------------
[•] Installed Module :
*. pyautodep 0.0.1
*. pip 23.0.1
*. pypisearch 1.3.5
*. requests 2.25.1
*. setuptools 58.1.0

---------------------
[•] Not Istalled Module :
*. fnmatch
*. os
*. setuptools setup, find_packages
*. argparse
*. importlib
```
