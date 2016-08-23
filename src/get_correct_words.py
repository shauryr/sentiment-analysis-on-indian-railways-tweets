from autocorrect import spell

input_path = "/home/shaurya/data/hackathon/input/final_tweets_parsed.txt"
output_path = '/home/shaurya/data/hackathon/output/parsed_output.txt'
file = open(input_path, 'r')
output_file = open(output_path, 'w')
for i in file:
    list_i = i.split(' ')
    for j in list_i:
        output_file.write(spell(j) + ' ')
    output_file.write('\n')

output_file.close()
