# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

"""Pipeline sequentially applies a list of transforms and a final estimator.
TfidfVectorizer builds a vocabulary
max_df : float in range [0.0, 1.0] or int, default=1.0
    used to ignore terms that have a document frequency higher than the given threshold
min_df : float in range [0.0, 1.0] or int, default=1 
    used to ignore terms that have a document frequency lower than the given threshold.
LinearSVC creates the SVC classifier
C : float, optional (default=1.0)
    Penalty parameter C of the error term.
"""
def buildPipeline(min_df, max_df, c):
    return Pipeline([('vect', TfidfVectorizer(min_df=min_df, max_df=max_df)),('clf', LinearSVC(C=c)),])

"""Exhaustive search over specified parameter values for an estimator
GridSearchCV(estimator, param_grid, n_jojs)
The parameters of the estimator used to apply these methods are optimized by
cross-validated grid-search over a parameter grid.
param_grid : dict or list of dictionaries
    Dictionary with parameters names (string) as keys and lists of parameter settings to
    try as values, or a list of such dictionaries, in which case the grids spanned by
    each dictionary in the list are explored. This enables searching over any sequence of parameter settings.
n_jobs : int, default=1
    Number of jobs to run in parallel.
"""
def buildGrid(pipeline, parameters):
    return GridSearchCV(pipeline, parameters, n_jobs=-1)