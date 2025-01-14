# Copyright 2024-2025 NetCracker Technology Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List
import re

from setuptools import setup, find_packages


def get_content(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def get_requirements(path: str) -> List[str]:
    return get_content(path).split('\n')


with open('git_system_follower/package_manager/__init__.py') as initfile:
    version = re.search(r'__version__ = \'(.*?)\'', initfile.read()).group(1)


setup(
    name='git-system-follower',
    packages=find_packages(exclude=("docs", "requirements")),
    version=version,
    description='',
    long_description=get_content('README.md'),
    long_description_content_type="text/markdown",
    author='Vladislav Kishkin',
    author_email='vladislav.kishkin01@gmail.com',
    url='TBD',
    license=get_content('LICENSE'),
    install_requires=get_requirements('requirements/requirements.txt'),
    extras_require={
        'dev': get_requirements('requirements/requirements_dev.txt')
    },
    setup_requires=[
        'wheel==0.37.1'
    ],
    entry_points={
        'console_scripts': [
            'git-system-follower = git_system_follower.cli:cli',
            'gsf = git_system_follower.cli:cli',
        ],
    },
    tests_require=[],
    test_suite='tests',
    python_requires='>=3.10'
)
