from setuptools import setup, find_packages

version = '0.1'

setup(name='cyanure',
      version=version,
      description="Multi-Purpose Artificial Inelegance Project",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='irc bot ai markov',
      author='Alexandre Gauthier',
      author_email='alex@lab.underwares.org',
      url='http://github.com/mrdaemon/cyanure2',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
