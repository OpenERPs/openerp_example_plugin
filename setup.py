from setuptools import setup, find_packages

setup(
    name="openerp_example_plugin",
    version="0.1.0",
    author="Rudransh",
    author_email="jrudeansh@pm.me",
    description="This is an example plugin for OpenERP.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OpenERPs/openerp_example_plugin.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # "fastapi", Dont include it
        "nothing==0.0.3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
