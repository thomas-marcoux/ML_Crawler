# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:57:19 2016

@author: Sorel
"""

import scrapy
import sys
import os

from pages import pages, get_ids

# Web crawler used to gather reviews from one specific product page
class MySpider(scrapy.Spider):
    name = 'steam_spider'
    base_url ='http://steamcommunity.com/app/%s/homecontent/?userreviewsoffset=%s&p=%s&workshopitemspage=%s&readytouseitemspage=%s&mtxitemspage=%s&itemspage=%s&screenshotspage=%s&videospage=%s&artpage=%s&allguidepage=%s&webguidepage=%s&integratedguidepage=%s&discussionspage=%s&numperpage=10&browsefilter=toprated&browsefilter=toprated&l=english&appHubSubSection=10&filterLanguage=default&searchText=&forceanon=1'
    i = 1
    max = 100
    ids = []
    j = 0
    content = {}
    
    # Start the request and returns a scrapy Request object
    def start_requests(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        # Get the IDs of reviews labelled as negative. This has to be changed in the code to grab mixed and positive reviews
        self.ids = get_ids(pages, "neg")
        for i in self.ids:
            self.content[i] = ""
        # Skip existing pages
        self.skip()
        # If pages need to be captured, do so
        if self.j < len(self.ids):
            yield scrapy.Request(url=self.base_url % (self.ids[self.j], 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), callback=self.parse)
            
    # Parse the user reviews from the web page and write them to a file
    def parse(self, response):
        buff = ""
        for review in response.css('div.apphub_UserReviewCardContent'):            
            buff += review.css('div.apphub_CardTextContent').extract_first()
        # When we are done gathering: write
        if buff == "" or self.i == self.max:
            open(self.ids[self.j] + '.html', 'w').write(self.content[self.ids[self.j]])
            self.i = 1
            self.j += 1
            self.skip()
            if self.j < len(self.ids):
                yield scrapy.Request(url=self.base_url % (self.ids[self.j], 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), callback=self.parse)
        else:
            self.content[self.ids[self.j]] += buff
            self.i += 1
            i = self.i
            yield scrapy.Request(url=self.base_url % (self.ids[self.j], (i-1)*10, i, i, i, i, i, i, i, i, i, i, i, i), callback=self.parse)
    
    # Skip already existing files
    def skip(self):
        while self.j < len(self.ids) and os.path.exists(self.ids[self.j] + '.html'):
            print 'skipping ' + self.ids[self.j] + '.html (already exists)'
            self.j += 1
