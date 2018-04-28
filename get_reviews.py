# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:19:29 2016

@author: Thomas
"""
import os
from urllib2 import Request, build_opener
from bs4 import BeautifulSoup
from pages import pages

def get_reviews(review_folder):
    if not os.path.exists(review_folder):
        os.makedirs(review_folder)
    for page, rating in pages.items():
        rating_folder = os.path.join(review_folder, rating)
        output = os.path.join(rating_folder, page + '.html')
        if not os.path.exists(rating_folder):
            os.makedirs(rating_folder)
        if not os.path.exists(output):
            opener = build_opener()
            url = 'http://steamcommunity.com/app/' + page + '/reviews/?browsefilter=toprated'
            print("Downloading %s" % url)
            html_content = opener.open(Request(url)).read()
            soup = BeautifulSoup(str(html_content), "lxml")
            open(output, 'w').write(str(soup.findAll("div", {"class" : "apphub_CardTextContent"})))

