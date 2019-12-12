import numpy as np
import os, sys
import pdb
import matplotlib
import matplotlib.pyplot as plt

TRAIN_PATH = './aclImdb/train/'
VAL_PATH = './aclImdb/test/'

TRAIN_LIST = os.listdir(TRAIN_PATH)
VAL_LIST = os.listdir(VAL_PATH)

print(TRAIN_LIST)
