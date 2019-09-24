#!/usr/bin/python3

import subprocess

def SoftwareChecker(package):
 software = subprocess.run('rpm -qa | grep %s' % (package), stdout=subprocess.PIPE, shell=True)
 print(software.stdout.decode())

SoftwareChecker(input("enter software package name: "))
