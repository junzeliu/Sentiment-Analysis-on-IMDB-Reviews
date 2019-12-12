import numpy as np
import os, sys
import pdb
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer

TRAIN_PATH = './aclImdb/train/'
TEST_PATH = './aclImdb/test/'


# ====================== 0. Loading and Preprocess Data ========================
# each data sample (review) is a document of words
# each review is either negative (0) or positive (1)
reviews_train = load_files(TRAIN_PATH)
data_train, targets_train = reviews_train.data, reviews_train.target
print("Number of reviews: {}".format(type(data_train))) # 25000
print("Samples per class (training): {}".format(np.bincount(targets_train)))

reviews_test = load_files(TEST_PATH)
data_test, targets_test = reviews_test.data, reviews_test.target
print("Number of reviews: {}".format(type(data_train))) # 25000
print("Samples per class (training): {}".format(np.bincount(targets_train)))

# remove line breakers
data_train = [review.replace(b"<br />", b" ") for review in data_train]
data_test = [review.replace(b"<br />", b" ") for review in data_test]

# =========================== 1. Vectorize reviews =============================

vect = CountVectorizer()
vect.fit(data_train)
feature_names = vect.get_feature_names()
print("Size of vocabulary: {}".format(len(feature_names)))

X_train = vect.transform(data_train) # 25000 x 74849





pdb.set_trace()

