from setuptools import find_packages, setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='leather',
    version='0.3.5',
    description='Python charting for 80% of humans.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Christopher Groskopf',
    author_email='chrisgroskopf@gmail.com',
    url='https://leather.readthedocs.io/',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=['tests', 'tests.*']),
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
            'lxml>=3.6.0',
            'cssselect>=0.9.1',
        ],
    }
)
