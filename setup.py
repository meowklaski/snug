from setuptools import setup
from pathlib import Path

import snug


def read(fname):
    return (Path(__file__).parent / fname).read_text()


setup(
    name='snug',
    version=snug.__version__,
    description=snug.__description__,
    license='MIT',
    long_description=read('README.rst') + '\n\n' + read('HISTORY.rst'),
    url='https://github.com/ariebovenberg/snug',

    author=snug.__author__,
    author_email='a.c.bovenberg@gmail.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=['api-wrapper', 'http', 'generators', 'async',
              'graphql', 'rest', 'rpc'],
    python_requires='>=3.5',
    py_modules=('snug',),
)
