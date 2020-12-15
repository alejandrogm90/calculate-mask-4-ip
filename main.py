#!/usr/bin/env python3

#
#
#       Copyright 2020 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import sys
import math 

# VARIBLES GLOBALES
LOCAL_BROADCAST = "255.255.255.0"
DEFAULT_GATEWAY = "192.168.1.1"

# CLASES
class myIP:
    def __init__(self, numero="0.0.0.0"):
        self.direction = list()
        self.direction.append(int(numero.split(".")[0]))
        self.direction.append(int(numero.split(".")[1]))
        self.direction.append(int(numero.split(".")[2]))
        self.direction.append(int(numero.split(".")[3]))

    def add(self):
        if self.direction[3] < 255:
            self.direction[3] = self.direction[3] + 1
        elif self.direction[2] < 255:
            self.direction[2] = self.direction[2] + 1
            self.direction[3] = 0
        elif self.direction[2] < 255:
            self.direction[1] = self.direction[1] + 1
            self.direction[3] = 0
            self.direction[2] = 0
        elif self.direction[0] < 255:
            self.direction[0] = self.direction[0] + 1
            self.direction[3] = 0
            self.direction[2] = 0
            self.direction[1] = 0
        if self.direction[3] > 255:
            self.direction[0] = 0
            self.direction[3] = 0
            self.direction[2] = 0
            self.direction[1] = 0
        else:
            return False
        return True

    def getFinalDirection(self,total):
        for elemento in range(0,total):
            self.add()
        return self

    def __str__(self):
        return str(self.direction[0])+"."+str(self.direction[1])+"."+str(self.direction[2])+"."+str(self.direction[3])

# FUNCIONES
def printOutPut(start_ip, final_range):
    total_ips = int(math.pow(2, final_range))
    print("Total IPs: "+str(total_ips))
    print("Initial IP: "+str(start_ip))
    end_ip = start_ip.getFinalDirection(total_ips)
    print("Final IP: "+str(end_ip))

def paramError():
    print(sys.argv[0]+" IP/MASK")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        paramError()
        exit -1

    ip1 = myIP(sys.argv[1].split('/')[0])
    printOutPut(ip1,int(sys.argv[1].split('/')[1]))


    


