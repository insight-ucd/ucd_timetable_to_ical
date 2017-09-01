import sys
from setuptools import setup

setup(
    name="UCD_timetable_to_ical",  # what you want to call the archive/egg
    version="0.1",
    packages=["src"],  # top-level python modules you can import like
    #   'import foo'
    dependency_links=[],  # custom links to a specific project
    extras_require={},  # optional features that other packages can require
    #   like 'helloworld[foo]'
    package_data={},
    author="Aonghus Lawlor",
    author_email="aonghus.lawlor@ucd.ie",
    description="Convert the UCD Infohub Timetable to iCal",
    license="GPL3",
    keywords="icalendar",
    url="https://git.ucd.ie/aonghuslawlor/ucd_timetable_to_ical/tree/master",
    entry_points={
        "console_scripts": [  # command-line executables to expose
            "timetable_to_ical = src.ical:main",
        ],
    },
    install_requires=[
        'pandas',
        'icalendar'
    ]
)
