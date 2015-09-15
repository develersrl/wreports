from setuptools import setup, find_packages

setup(name='wreports',
      version='0.1.0',
      author='',
      description='wreports description',
      long_description=open('README.rst').read(),
      license='LICENSE.txt',
      keywords="",

      # package source directory
      package_dir={'': 'src'},
      packages=find_packages('src', exclude='docs')


    # configure the default test suite
    , test_suite='tests.suite'

)