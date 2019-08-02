#Uploading the package
#Remove build,dist,sammi.egg-info
#Define new version
#python setup.py sdist bdist_wheel #Writes the package
#python -m twine upload dist/* #Uploads
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sammi",
    version="0.1.2",
    author="Andre Schultz",
    author_email="schultzdre@gmail.com",
    description="A wrapper for running the Semi-Automated Metabolic Map Illustrator (SAMMI) using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schultzdre/SAMMIpy.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={'sammi': ['sammi.py','browser/demo.json','browser/helpfunctions.js','browser/index.html','browser/index_load.html','browser/sammi.css','browser/simulationfunctions.js','browser/uploaddownload.js']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)