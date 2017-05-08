#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

base = 'Win32GUI' if sys.platform == 'win32' else None

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
	packages=[],
	excludes=[],
	includes=[],
	include_files=[]
)

executables = [
    Executable('core.pyw', base=base, icon='data/rocket.ico')
]

setup(
	name="Astro Lords - BrokeYourBike",
	version="1.0",
	description="Developed by Ivan Stasiuk",
	options=dict(build_exe=buildOptions),
	executables=executables
)


input("Press Enter")
