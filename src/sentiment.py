import urllib
import json

file = open('/home/shaurya/data/hackathon/input/final_tweets.txt', 'r')
output_file = open('/home/shaurya/data/hackathon/input/analysis_tweets.txt', 'w')
for line in file:
    print line
    data = urllib.urlencode({"text": line})
    u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
    the_page = u.read()
    output_file.write(line + '\t' + the_page + '\n')
    # print type(u)






    #
    # data = urllib.urlencode({"text": "I'm a very good boy "})
    # u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
    # the_page = u.read()
    # print the_page
