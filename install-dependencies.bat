@echo off
title Installing dependencies
color 07
echo Installing dependencies, please wait...
py -2.7 -m pip install --upgrade Pillow==6.2.2
timeout 2 > nul