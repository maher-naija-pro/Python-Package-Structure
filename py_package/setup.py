from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='py_package',
      version='0.1',
      description='py_package',
      url='http://github.com/',
      author='maher',
      author_email='maher.naija@gmail.Com',
      license='MIT',
      packages=['py_package'],
      install_requires=[
          'boto3',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['bin/py_package_my_function'],
      zip_safe=False)
