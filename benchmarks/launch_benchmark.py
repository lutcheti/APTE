#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import os
import sys
import glob                     # for regexp
from time import clock, time
import subprocess
from datetime import datetime

## I reuse an old script (for SPEC)

def main():
    HEAD = " " + "#"*10 + " "
    HEADA = " " + "#"*5 + " "
    IND = " " * 50
    list_tests = glob.glob('../Example/Simple_*.txt')
    list_binaries = glob.glob('../apte_*')
    log_all = open("log/results_" + str(datetime.now()) + ".log", "w+")
    def print_all(s):
#        print s
        log_all.write(s)
        log_all.flush()

    for file in list_tests:
        t_name = file.split("/Example/")[1].split(".txt")[0]
        print_all(HEAD + "Starting to benchmark: " + t_name + HEAD + "\n")
        print_all(IND + str(datetime.now()) + "\n") # timestamp

        for binary in list_binaries:
            b_name = binary.split('../')[1]
            print_all(HEADA + "Starting to benchmark: " + b_name + HEADA + "\n")
            log_t_b = open("log/" + t_name + "_" + b_name + ".log", "w+")
            print_all(IND + str(datetime.now()) + "\n")
            log_t_b.write(IND + str(datetime.now()))
            proc = subprocess.Popen([binary, file],
                                    stdout=subprocess.PIPE)
            for line in iter(proc.stdout.readline,''):
                line_t = line.rstrip()
                if line_t[0:3] == "Res":
                    print_all(line_t + "\n")
                else:
                    print(line_t)
                log_t_b.write(line_t + "\n")
                log_t_b.flush()

main()
