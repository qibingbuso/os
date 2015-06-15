# -*- coding: utf-8 -*-

import json
import requests

def geneEachHelp(keyWord):
    print 'geneHelp...'
    url = 'https://www.google.com/?gws_rd=ssl#newwindow=1&q=%s+site:cateee.net' %(keyWord)
    html = requests.get()


if __name__=='__main__':
    geneHelp()
