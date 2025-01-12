# clic Full Guide

This guide is going to assist you on how to use clic (Command Line Interface Calculator) and how to setup and install.

## 1 - Installation

clic offers a .deb package at the releases, currently it is the only method to use clic besides make.

### 1.1 - dpkg/pkg/apt

To download with any package manager based on dpkg, you can use these commands below.

* x.y being the version number. e.g: clic_1.2.deb, etc

**dpkg**
> dpkg -i ./clic_x.y.deb

**pkg**
> pkg install ./clic_x.y.deb 

**apt**
> apt install ./clic_x.y.deb

### 1.2 - make

clic is also runnable with make, and also debuggable with make. 

~~To run clic with make, do:

~~> make~~

~~On the clic folder.~~
* Cannot use make to run clic anymore, as it has been switched to a full command line utility.


You can also debug clic, using make + parameters.

Debug make parameters are as:

> make venv
* To create a python virtual environment

> make run
* To run the python script

> make install
* To install dependencies in the virtual environment

> make clean
* To clean up temporary files

> make package
* To create a dpkg of clic

## 2 - Use

Using clic is straightforward. Here's how:

### 2.1 - clic on CLI

To execute clic, you need to install clic via dpkg or any supported package manager.

To use clic, do:

clic -e "EQUATION"

A equation can be like:

clic -e "20*2-10"





