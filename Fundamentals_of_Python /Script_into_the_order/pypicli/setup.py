import setuptools

# name='Click_Advanced_Usage',
setuptools.setup(
    name='pypicli_chaz',
    version='0.0.1',
    author='bestony',
    description='pypi cli example',
    long_description='#pypicli',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    py_modules=["pypicli"],
    package_dir={"": "src"},
    install_requires=["Click"],
    entry_points={'console_scripts': ['pypix = cli:hello']}
)
