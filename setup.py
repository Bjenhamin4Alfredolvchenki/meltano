#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'aiohttp',
    'backoff',
    'dbt',
    'gitpython',
    'markdown',
    'pandas',
    'psycopg2',
    'pypika',
    'python-dotenv',
    'pyyaml',
    'snowflake-connector-python',
    'snowflake-sqlalchemy',
    'sqlalchemy',
]

api_requires = [
    'flask',
    'flask-cors',
    'flask-sqlalchemy',
]

cli_requires = [
    'click',
]

setup(
    name="meltano",
    version="0.0.1",
    author='Meltano Team & Contributors',
    author_email="meltano@gitlab.com",
    description="Meltano",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/meltano/meltano",
    package_dir={'': 'src'},
    packages=find_packages(),
    package_data={
        'meltano.api': [
            'node_modules',
        ]
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    # run `make requirements.txt` after editing
    install_requires=requires,
    extras_require={
        'api': api_requires,
        'cli': cli_requires,
        'all': [
            *api_requires,
            *cli_requires
        ],
    },
    entry_points={
        'console_scripts': [
            "meltano = meltano.cli:main [cli]"
        ]
    }
)