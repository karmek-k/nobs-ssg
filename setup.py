import setuptools


with open('README.md') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='nobs-ssg-karmek-k',
    version='0.0.2',
    author='Bartosz Gleń',
    description='Nobs Static Site Generator, fast and easy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/karmek-k/nobs-ssg',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
