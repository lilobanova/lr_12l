#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def el_min(i, mini, list):
    if i == len(list):
        return mini
    else:
        if list[i] < mini:
            mini = list[i]
        i += 1
    return el_min(i, mini, list)


if __name__ == '__main__':
    Lst = input("Введите = ").split()
    frm = 2
    print(el_min(frm - 1, Lst[frm - 1], Lst))
