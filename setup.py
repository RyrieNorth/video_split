#!/usr/bin/env python
import os
from setuptools import setup

if os.name == "nt":  # Windows 系统
    package_data = {"": ["tools/ffmpeg.exe"]}
else:
    package_data = {"": ["tools/ffmpeg"]}

setup(
    name="video_split",
    version="0.1",
    license="MIT",
    url="https://github.com/RyrieNorth/video_split",
    description="A tool for video_split",
    platforms=["any"],
    author="RyrieNorth",
    author_email="bk15018708480@gmail.com",
    install_requires=["pymediainfo"],
    packages=["video_split"],
    package_data=package_data,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "vl_split = video_split.main:run",
        ],
    },
)
