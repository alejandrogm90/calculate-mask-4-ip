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
class direccionIP:
    def __init__(self, numero="0.0.0.0"):
        self.direccion = list()
        self.direccion.append(int(numero.split(".")[0]))
        self.direccion.append(int(numero.split(".")[1]))
        self.direccion.append(int(numero.split(".")[2]))
        self.direccion.append(int(numero.split(".")[3]))

    def sumar(self):
        if self.direccion[3] < 255:
            self.direccion[3] = self.direccion[3] + 1
        elif self.direccion[2] < 255:
            self.direccion[2] = self.direccion[2] + 1
            self.direccion[3] = 0
        elif self.direccion[2] < 255:
            self.direccion[1] = self.direccion[1] + 1
            self.direccion[3] = 0
            self.direccion[2] = 0
        elif self.direccion[0] < 255:
            self.direccion[0] = self.direccion[0] + 1
            self.direccion[3] = 0
            self.direccion[2] = 0
            self.direccion[1] = 0
        if self.direccion[3] > 255:
            self.direccion[0] = 0
            self.direccion[3] = 0
            self.direccion[2] = 0
            self.direccion[1] = 0
        else:
            return False
        return True

    def devolverConRango(self,total):
        for elemento in range(0,total):
            self.sumar()
            #print("----"+str(self))
        return self

    def __str__(self):
        return str(self.direccion[0])+"."+str(self.direccion[1])+"."+str(self.direccion[2])+"."+str(self.direccion[3])

# FUNCIONES
def getRango(start_ip, rango):
    total = int(math.pow(2, rango))
    print("Total de IPs del rango: "+str(total))
    print("IP inicial: "+str(start_ip))
    end_ip = start_ip.devolverConRango(total)
    print("IP final: "+str(end_ip))

def paramError():
    print(sys.argv[0]+" IP/MASK")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        paramError()
        exit -1

    ip1 = direccionIP(sys.argv[1].split('/')[0])
    getRango(ip1,int(sys.argv[1].split('/')[1]))


    


