from setuptools import setup, find_packages

setup(
    name="facebook_agent",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "flask==2.3.2",
        "flask-cors==3.0.10",
    ],
)