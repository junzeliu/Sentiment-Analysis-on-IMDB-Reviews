import numpy as np
import os, sys
import pdb
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import load_files

TRAIN_PATH = './aclImdb/train/'
VAL_PATH = './aclImdb/test/'

# TRAIN_LIST = os.listdir(TRAIN_PATH)
# VAL_LIST = os.listdir(VAL_PATH)

# print(TRAIN_LIST)

reviews_train = load_files(TRAIN_PATH)
data_train, targets_train = reviews_train.data, reviews_train.target
print("Number of reviews: {}".format(type(data_train)))

# remove line breakers
data_train = [review.replace(b"<br />", b" ") for review in data_train]

pdb.set_trace()

