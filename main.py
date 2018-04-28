# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:19:29 2016

@author: Thomas
"""

from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
#from get_reviews import get_reviews
from functions import buildPipeline, buildGrid
from sklearn import metrics
import matplotlib.pyplot as plt
import time 

if __name__ == "__main__":
    review_folder = "reviews"
    grid_parameters = {'vect__ngram_range':[(1, 1), (1, 2)],}
    min_df = 2
    max_df = 0.80
    c = 1000
    test_size = 0.20
    #print("Fetching reviews")
    #get_reviews(review_folder)
    print("Loading reviews")
    dataset = load_files(review_folder, shuffle=False)
    print("Number of reviews: %d" % len(dataset.data))
    print("Splitting data")
    X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=test_size, random_state=None)
    print("Building classifier")    
    pipeline = buildPipeline(min_df, max_df, c)
    grid_search = buildGrid(pipeline, grid_parameters)
    print("Fitting data (started at " + time.strftime('%X %x %Z') + ")") 
    grid_search.fit(X_train, y_train)
    print("(ended at " + time.strftime('%X %x %Z') + ")") 
    print("Making prediction") 
    prediction = grid_search.predict(X_test)
    print(metrics.classification_report(y_test, prediction, target_names=dataset.target_names))
    print("Plottiong confusion matrix") 
    cm = metrics.confusion_matrix(y_test, prediction)
    print(cm)    
    plt.matshow(cm)
    plt.show()
