from setuptools import setup, find_packages

setup(name='codebottle',
      version='0.0.1',
      description="A Python library to interact with CodeBottle's API",
      url='https://github.com/codebottle-io/codebottle-python',
      author='Luke J.',
      author_email='support@codebottle.io',
      license='GNU',
      packages=find_packages(),
      install_requires=['requests'],
      include_package_data=True,
      zip_safe=False)
