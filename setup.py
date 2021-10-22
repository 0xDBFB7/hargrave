import setuptools
#
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hargrave",
    # version="0.0.1",
    # author="Daniel Correia",
    # author_email="therobotist@gmail.com",
    # description="A wrapper around flaport/FDTD for PCB simulations.",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=['hargrave_base', 'hargrave_drivers', 'hargrave_language_bindings', 'hargrave_modules', 'hargrave_standards'],
    # classifiers=[
    # ],
    python_requires='>=3.6',
)
