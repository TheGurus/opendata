import setuptools

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

requirements = [
    'requests',
]

setuptools.setup(
    name='gurus-opendata',
    version='0.0.2',
    author='The Gurus',
    author_email='opendata@thegurus.tech',
    description='We get Data from the Internet and We make it available to the World',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/TheGurus/opendata',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
