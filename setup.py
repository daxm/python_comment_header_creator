from setuptools import setup, find_packages

__author__ = "Dax Mickelson"
__author_email = "dmickels@cisco.com"
__license__ = "BSD"

setup(
    name='comment_header_creator',
    version='20200116.0',
    description="Create nicely formatted comment strings to be used as headers/seperators in your code.",
    long_description="""Create nicely formatted comment strings to be used as headers/seperators in your code.""",
    url='https://github.com/daxm/python_comment_header_creator/',
    author='Dax Mickelson',
    author_email='dmickels@cisco.com',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    keywords='header comment title seperator organize',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[],
    python_requires='>=3.6',
    package_data={},
    data_files=None,
)
