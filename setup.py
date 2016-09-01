from setuptools import setup

setup(name='codebottle',
      version='0.0.1',
      description="A Python library to interact with CodeBottle's API",
      url='https://github.com/codebottle-io/codebottle-python',
      author='Luke J.',
      author_email='support@codebottle.io',
      license='GNL',
      packages=['codebottle'],
      install_requires=['requests'],
      include_package_data=True,
      zip_safe=False)