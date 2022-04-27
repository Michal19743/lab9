# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:08:06 2022

@author: Student
"""

import mojeklasy

def testy():
    pass

print("Zadanie 4 / zadanie 1")
pkt1 = mojeklasy.Punkt2D(1,2)
pkt1.drukuj()
pkt1.zeruj()
pkt1.drukuj()
print()

print("Zadanie 4 / zadanie 2")
pkt2 = mojeklasy.Punkt3D(1,2,3)
pkt2.drukuj()
pkt2.zeruj()
pkt2.drukuj()
print()

print("Zadanie 4 / zadanie 3")
dlOdc = mojeklasy.Odcinek(1,2,2,6)
dlOdc.drukuj()
print()

if __name__ == "_main_":
    testy()
