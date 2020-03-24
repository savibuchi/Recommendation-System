#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:49:42 2017

@author: savi
"""

from collections import defaultdict
import surprise
import pandas as pd
from pydataset import data
from surprise import SVD
from surprise import Dataset
from surprise import evaluate, print_perf
from surprise import Reader
import numpy as np


da = pd.read_csv('df2.csv',encoding='latin')
df=pd.DataFrame(da)



reader = Reader(rating_scale=(1, 5))
# The columns must correspond to user id, item id and ratings (in that order).
da1 = Dataset.load_from_df(df[['username', 'unqiue_hotel', 'rating']], reader)


# First train an SVD algorithm on the trip advisor hotel data
trainset = da1.build_full_trainset()
algo = SVD()
algo.train(trainset)

# Than predict ratings for all pairs (u, i) that are NOT in the training set.
testset = trainset.build_anti_testset()
predictions = algo.test(testset)


def get_top_n(predictions, n=12850):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n




top_n = get_top_n(predictions, n=12850)

#writing the file in csv format
(pd.DataFrame.from_dict(data=top_n, orient='index').
to_csv('dict_file.csv', header=False))


    
    
  




  
    
    
#NOT USED THIS PART - ignore this part
    
    uuid.append(uid)
    rati.append(user_ratings)
for uid, user_ratings in top_n.items():
    print(uid,user_ratings, [iid for (iid, _) in user_ratings])
    
uuid
uuid= []
rati=[]
mat=[[]]
mat1=[[]]
for uid, user_ratings in top_n.items():
    mat=[uid,user_ratings]
    mat1.append(mat)

df3=pd.DataFrame(mat1)

# Print the recommended items for each user
for uid, user_ratings in top_n.items():
    print(uid,user_ratings)





t