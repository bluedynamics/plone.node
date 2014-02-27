from setuptools import find_packages
from setuptools import setup

import os

version = '1.0-alpha'
shortdesc = 'Node based Content-Types framework for Plone'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()

setup(
    name='plone.node',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        "Framework :: Plone",
    ],
    keywords='',
    author='BlueDynamics Alliance',
    author_email='dev@bluedynamics.com',
    license='GPLv2',
    url='https://pypi.python.org/pypi/plone.node',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['plone', ],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'node.ext.zodb',
        'Zope2',
        'Products.CMFCore',
        'Products.CMFDefault',
        'Products.CMFDynamicViewFTI',
        'setuptools',
        'zope.container',
        'zope.interface',
    ],
    extras_require={
        'test': [
            'interlude',
            'plone.testing',
            'ipdb',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
