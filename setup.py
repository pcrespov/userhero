from pathlib import Path
from setuptools import setup, find_packages

install_requirements = []
test_requirements = [
    'pytest'
]

readme = Path( here / "README.md" ).read_text()

setup(
    name='userhero',
    version='0.1.0',
    author="Pedro Crespo (pcrespov)",
    description="Simple library of fake users with hero profiles",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    long_description=readme,
    license="MIT license",
    install_requires=install_requirements,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
        '': [
            '*.json',
        ]
    },
    test_suite='tests',
    tests_require=test_requirements,
    extras_require= {
        'test': test_requirements
    },
    zip_safe=False
)