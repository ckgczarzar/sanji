from setuptools import setup

setup(name="sanji",
      version="0.1",
      description="Sanji SDK",
      url="https://github.com/Sanji-IO",
      author="Sanji Team",
      author_email="sanji@moxa.com",
      license="MOXA",
      packages=["sanji", "sanji.connection"],
      zip_safe=False,
      install_requires=["voluptuous"]
      )
