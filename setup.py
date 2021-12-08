from setuptools import setup, find_packages

setup(
    name='pyqt-popup-graphics-view',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Popup QGraphicsView (Image will pop up when move the mouse cursor inside the QGraphicsView)',
    url='https://github.com/yjg30737/pyqt-popup-graphics-view.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)