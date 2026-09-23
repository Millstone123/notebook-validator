from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension("nb._nbprofile", ["native/profile.c"]),
    ],
)
