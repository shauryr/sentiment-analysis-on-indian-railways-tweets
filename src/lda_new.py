from gensim import corpora, models, similarities
from itertools import chain
from stop_words import get_stop_words

""" DEMO """
# documents = ["Human machine interface for lab abc computer applications",
#              "A survey of user opinion of computer system response time",
#              "The EPS user interface management system",
#              "System and human system engineering testing of EPS",
#              "Relation of user perceived response time to error measurement",
#              "The generation of random binary unordered trees",
#              "The intersection graph of paths in trees",
#              "Graph minors IV Widths of trees and well quasi ordering",
#              "Graph minors A survey"]

documents = []

file = open('/home/shaurya/data/hackathon/input/negative_tweets.txt', 'r')

for line in file:
    documents.append(line)

print len(documents)
# remove common words and tokenize
stoplist = get_stop_words('en')

# = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]

# remove words that appear only once
all_tokens = sum(texts, [])
# TODO
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 0)
texts = [[word for word in text if word not in tokens_once] for text in texts]

# Create Dictionary.
id2word = corpora.Dictionary(texts)

# Creates the Bag of Word corpus.
mm = [id2word.doc2bow(text) for text in texts]
# print mm
# Trains the LDA models.
lda = models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=50, \
                               update_every=1, chunksize=10000, passes=10)

# Prints the topics.
# for top in lda.print_topics(num_topics=5, num_words=100):
#     print top
# print

# Assigns the topics to the documents in corpus
lda_corpus = lda[mm]

# print lda
# print lda_corpus
count = 0
# for i in lda_corpus:
#     print i
#     print documents[count]
#     count += 1
# print count

# print len(scores)
# print(lda.print_topics(num_topics=25, num_words=10))
# print lda.show_topics(num_topics=50, num_words=10, formatted=True)

# output_lda = '/home/shaurya/data/hackathon/output/lda_out_negative_tweets.txt'
# file_lda = open(output_lda, 'w')
for i in lda.show_topics(num_topics=50, num_words=10, formatted=True):
    # file_lda.write(i)
    # file_lda.write('\n')
    print i

# file_lda.close()
