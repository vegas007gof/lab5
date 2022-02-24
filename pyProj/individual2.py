#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    x1 = int(input("Value of x1? "))
    y1 = int(input("Value of y1? "))
    x2 = int(input("Value of x2? "))
    y2 = int(input("Value of y2? "))
    if x1 == x2:
        print("по оси oy точки паралельны")
    elif y1 == y2:
        print("по оси ox точки паралельны")
    else:
        print("точки не паралельны")