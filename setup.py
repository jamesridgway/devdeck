from setuptools import setup, find_packages
import subprocess


def get_version():
    process = subprocess.Popen(["git", "describe", "--always", "--tags"], stdout=subprocess.PIPE, stderr=None)
    last_tag = process.communicate()[0].decode('ascii').strip()
    if '-g' in last_tag:
        return last_tag.split('-g')[0].replace('-', '.')
    else:
        return last_tag


with open('requirements.txt') as f:
    install_reqs = f.read().splitlines()

setup(
    name='devdeck',
    version=get_version(),
    description="A developer's approach to using a Stream Deck.",
    long_description=open('README.md').read(),
    author='James Ridgway',
    url='https://github.com/jamesridgway/devdeck',
    license='MIT',
    packages=find_packages(),
    scripts=['bin/devdeck'],
    install_requires=install_reqs,
    include_package_data=True
)
