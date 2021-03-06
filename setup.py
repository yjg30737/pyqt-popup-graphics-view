from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-popup-graphics-view',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='GPL 3.0',
    packages=find_packages(),
    description='PyQt popup QGraphicsView (image will pop up when move the mouse cursor inside the QGraphicsView)',
    url='https://github.com/yjg30737/pyqt-popup-graphics-view.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8'
    ]
)