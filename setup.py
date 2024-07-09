from setuptools import setup, find_packages
import os


setup(
    name='library_authoring',
    version='0.1.0',
    include_package_data=True,
    install_requires=["setuptools"],
    requires=[],
    description='contains all the extra custom apps',
    packages=find_packages(exclude=["tests*", "tests"]),
    entry_points={
        "lms.djangoapp": [
        ],
        "cms.djangoapp": [
            "app = app.apps:AppConfig",
        ],
    }

)
