# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['networkx-stubs']

package_data = \
{'': ['*']}

extras_require = \
{':(python_version >= "2.7" and python_version < "2.8") or (python_version >= "3.3" and python_version < "3.5")': ['typing>=3.6,<4.0']}

setup_kwargs = {
    'name': 'networkx-stubs',
    'version': '0.0.1',
    'author': 'Florian Magin',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*',
}


setup(**setup_kwargs)
