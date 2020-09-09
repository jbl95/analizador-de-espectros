#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:15:11 2020

@author: Lauría Juan

Generador de señal senoidal - Módulo de función.
Procesamiento digital de señales.
19/08 - 1er clase

"""


import numpy as npy

def mi_func_sen (vmax, dc, ff, ph, nn, fs,):
    
   tt = npy.arange(nn/fs, step=1/fs)          
   
   xx = vmax * npy.sin((2 * npy.pi * ff * tt) + ph) + dc
   
   return tt,xx