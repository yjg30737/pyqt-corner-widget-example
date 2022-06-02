from setuptools import setup, find_packages

setup(
    name='pyqt-corner-widget-example',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt example which shows widget at the bottom-right corner of window (using event/geometry, '
                'no QGridLayout involved)',
    url='https://github.com/yjg30737/pyqt-corner-widget-example.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)