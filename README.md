# Post Quantum Key Exchange over the Internet

## Introduction

This README is a short introduction on the organisation of the software that comes with this package. All of the work available or work that has been done was done by Afraz Arif Khan on this repository. You can find numerous software implementations for Post Quantum Key Exchange methods on this repository. After February 2017, this repository will incrementally add software which is safe to use with TLS (Transport Layer Security). 


Current Post Quantum Cryptographic implementations:

- A Simple Provably Secure Key Exchange Scheme Based on the Learning with Errors Problem which can be found [here](https://eprint.iacr.org/2012/688)

## Dependencies

Before running any of the software available on this repository you must install python 2 on your platform. To install python 2 [here](https://www.python.org/downloads/) is the official python distribution for all platforms. 

Since the implementations given in this repository make use of TLS/SSL it is important to have the library in its default configuration installed on your platform. There will also be some utilisation of TLS and SSL in the command line to run the program with adjustable parameters but the exact syntax of running SSL/TLS is not necessary and as a result will not require you to familiarise yourself with all of the SSL commands.

### SSL for Python

To install SSL type the following command in terminal:

`$ pip install ssl`

### OpenSSL for the command line

#### Linux

`$ sudo apt-get install openssl`

#### Mac OS X

To install packages in the command line of MAC OS X it is important to have [brew](https://brew.sh/) installed. 

`$ brew instal openssl`

## Usage

First start by git cloning the repository to a directory you are comfortable with. To git clone please type the following in Terminal and to ensure that the submodules are in this repository:

`$ git --recurse-submodules clone https://github.com/Afrazinator/fypafraz.git`

After you have git cloned the repository then enter the repository using `cd`

`$ cd fypafraz`

If you do a simple `ls` it will show all the files in the repository.

To examine already existing implementations of PQC and how their performance has been optimised please do: 

`$ cd Existing\ Implementations`

To make use of implementations written in this repository:

`$ cd My\ Implementations/` NB: This is easier with Tab Completion in terminal

### Existing Implementations

There are 2 existing implementations and one of the focuses of this repo involves modifying them to improve their current performance. The 2 implementations are:

- [Frodo](https://github.com/lwe-frodo/lwe-frodo)
- [NewHope](https://github.com/tpoeppelmann/newhope)

Further examinations on how these 2 pieces of software will be optimised will be found in the existing implementations folder in this repository. The submodules are attached with their commit hash (at the time) for guaranteeing a baseline from the modified version of the code.

### My Implementations

#### Simple Key exchange in Python

Before executing the program you must at least have python 2.x in your system. The following dependency is required for generating the matrices in the program:

[Numpy](http://www.numpy.org/)

To install the dependency please use `pip` : 

`$ python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose` as seen on [this website](https://scipy.org/install.html)

As referred to in the introduction section this is based on a simple key exchange with the learning with errors problem. If you followed the above steps and are in _My Implementations_ then to run the simple key exchange please type the following in terminal:

`$ python simplekeyexchange.py`

Instead of running the key exchange once there is a shell script included to run the key exchange 'n' times. It can be used as:

`$ ./runsimplekexntimes n` <----- Here n specifies the number of times the key exchange runs before the program terminates.

If you are using a Unix based system you will need to make the shell script executable before running the above command, this can be achieved by:

`$ chmod u+x runsimplekexntimes`

If you wish to terminate execution on Linux or Unix you can use the Ctrl+X command to terminate the script.

#### Key Exchanges in C

If you have navigated to ~/fypafraz/My \Implementations/

Then you will see all the python folders and another folder called "Key Exchanges in C"

Type the following in the terminal:

`$ cd Key\ Exchanges\ in\ C/` <-- Again if you type 'K' press TAB and it will complete the rest in Terminal

Then type:

`$ ls`

It should list 2 folders and 1 shell script. The folders are:

- include (this includes the header files for the main script and the discrete gaussian scripts)
- src (this includes the C source files)

The shell script is called installationfordgs.sh

To use the shell script to install dependencies first type:

`$ chmod u+x installationfordgs.sh`

Then type:

`$ ./installationfordgs.sh`

To use the scripts you must navigate to the 'src' folder by doing `$ cd src`

In this folder before you compile the code there is a missing obj folder. There is a shell script available to install the obj directory for you:

To use the shell script type:

`$ chmod u+x createbojfiles.sh`

Then type:

`$ ./createobjfiles.sh`

This will create a folder called 'obj' and will install the relevant .o (object files). It is very important that this step is done before the program is compiled otherwise there will be linker errors.

Finally back in the 'src' folder type:

`$ make`

This will show a large number of warnings (unavoidable as the dgs library does not cater to the compiler warnings) but it should give no errors. If you see any errors then some of the installation steps have not worked and you may need to refer to them again. 

After you typed `make` there is an exectuable file available called 'jintailwe' (without any extensions)

Finally to run the code type:

`$ ./jintailwe`

This will run the key exchange and output whether the keys matched or not.
