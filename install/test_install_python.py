check = True
try:
    import scanpy
except:
    print('scanpy import error')
    check = False
try:
    import yaml
except:
    print('pyyaml import error')
    check = False

try:
    import numpy as np
except:
    print('numpy import error')
    check = False

try:
    import pandas as pd
except:
    print('pandas import error')
    check = False


try:
    import matplotlib
except:
    print('matplotlib import error')
    check = False

try:
    import scipy
except:
    print('scipy import error')
    check = False

try:
    import gseapy
except:
    print('gseapy import error')
    check = False

try:
    import anndata
except:
    print('anndata import error')
    check = False

try:
    import diopy
except:
    print('diopy import error')
    check = False

try:
    import bbknn
except:
    print('bbknn import error')
    check = False
try:
    import pyscenic
except:
    print('pyscenic import error')
    check = False

if check:
    print('successfully import all python pkgs')
