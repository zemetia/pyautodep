from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'Check and install python modules'
LONG_DESCRIPTION = 'Check every single imported python module(s) on your project and install it automatically'

# Setting up
setup(
    name="pyautodep",
    version=VERSION,
    author="Yoel Mountanus Sitorus",
    author_email="sclous2012@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=['pyautodep'],
    zip_safe=False,
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'package', 'autoinstall', 'pypi package'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
