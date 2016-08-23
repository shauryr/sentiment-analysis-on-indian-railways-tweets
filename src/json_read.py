import json as js

input_path = "/home/shaurya/data/hackathon/input/tweets.json"
data_file = open(input_path, 'r')
data = js.load(data_file)
output_path = "/home/shaurya/data/hackathon/input/tweets.txt"
file = open(output_path, 'w')
print len(data)
list_tweet = []
print  data[0]["tweet_text"]
for i in range(0, len(data)):
    print data[i]["tweet_text"]
    list_tweet.append(data[i]["tweet_text"].encode("utf-8"))
    file.write(data[i]["tweet_text"].encode("utf-8"))
    file.write('!@#$%^&*()' + '\n')
# print list_tweet

# print data


#https://socialmobileregistry.digitalgov.gov:443/api/v1/mobile_apps.json
