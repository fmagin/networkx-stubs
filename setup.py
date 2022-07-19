# -*- coding: utf-8 -*-

from setuptools import setup
import os

packages = \
['networkx-stubs']

package_data = \
{'': ['*']}



def find_stub_files():
    result = []
    for root, dirs, files in os.walk('networkx-stubs'):
        for file in files:
            if file.endswith('.pyi'):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result

test_requirements = [
    'mypy',
    'types-setuptools',
]

extras_require = {
    ':(python_version >= "2.7" and python_version < "2.8") or (python_version >= "3.3" and python_version < "3.5")': ['typing>=3.6,<4.0'],
    'test': test_requirements,
}

setup(
    name='networkx-stubs',
    version='0.0.2',
    author='Florian Magin',
    packages=packages,
    package_data={'networkx-stubs': find_stub_files()},
    extras_require=extras_require,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*',
    tests_require=test_requirements,
)
