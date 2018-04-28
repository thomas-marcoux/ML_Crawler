# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:19:29 2016

@author: Thomas
"""
import os
from urllib2 import Request, build_opener
from bs4 import BeautifulSoup
from pages import pages # Defined in steam_crawler/steam/spiders

# Populate review_folder with user reviews ordered by label
def get_reviews(review_folder):
    # If the folder does not exist, create it
    if not os.path.exists(review_folder):
        os.makedirs(review_folder)
    # For each web page, we attempt to output a file containing only the review's text
    for page, rating in pages.items():
        rating_folder = os.path.join(review_folder, rating)
        output = os.path.join(rating_folder, page + '.html')
        # Create the rating ('good', 'bad', 'mixed') folder if they do not exist
        if not os.path.exists(rating_folder):
            os.makedirs(rating_folder)
        # If the review file does not already exist, we create it and grab the review's text from the web page
        if not os.path.exists(output):
            opener = build_opener()
            url = 'http://steamcommunity.com/app/' + page + '/reviews/?browsefilter=toprated'
            print("Downloading %s" % url)
            html_content = opener.open(Request(url)).read()
            soup = BeautifulSoup(str(html_content), "lxml")
            open(output, 'w').write(str(soup.findAll("div", {"class" : "apphub_CardTextContent"})))

