import json as js

input_path = "/home/shaurya/data/hackathon/input/USA_apps.json"
data_file = open(input_path, 'r')
data = js.load(data_file)
output_path = "/home/shaurya/data/hackathon/input/json.txt"
file = open(output_path, 'w')
# print data
list_tweet = []
# print data
print  data['results'][0]['name']
print  data['results'][0]['short_description']
print  data['results'][0]['tags'][0]['tag_text']
print  data['results'][0]['tags'][1]['tag_text']
print  data['results'][0]['tags'][2]['tag_text']

count = 0

for i in range(0, len(data['results'])):
    file.write(data['results'][i]['name'] + '|')
    file.write((data['results'][i]['short_description'] + '|').encode("utf-8"))
    s = ''
    for j in range(0, len(data['results'][i]['tags'])):
        s = s + '&' + data['results'][i]['tags'][j]['tag_text']
    file.write(s + '\n')
    print count
    count += 1

    # for i in range(0, len(data)):
    #     print data[i]["tweet_text"]
    #     list_tweet.append(data[i]["tweet_text"].encode("utf-8"))
    #     file.write(data[i]["tweet_text"].encode("utf-8"))
    #     file.write('!@#$%^&*()' + '\n')
    # print list_tweet

    # print data


    # https://socialmobileregistry.digitalgov.gov:443/api/v1/mobile_apps.json
    # import urllib, json
    #
    # url = "https://socialmobileregistry.digitalgov.gov:443/api/v1/mobile_apps.json"
    # response = urllib.urlopen(url)
    # data = json.loads(response.read())
    # output_path = "/home/shaurya/data/hackathon/input/json.txt"
    # file = open(output_path, 'w')
    # print len(data)
    # print data[1]["name"]
    # print data[1]["short_description"]
