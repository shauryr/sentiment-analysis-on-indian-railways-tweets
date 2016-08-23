# sentiment-analysis-on-indian-railways-tweets
Sentiment analysis and LDA on Tweets about Indian Railways :

1. 2000 Tweets on the twitter handle have been fetched for the handle '@RailMinIndia'.
2. The tweets are mostly complaints against the Rail Ministery of India. Also, tweets may be annoucements about railways.
3. Tried to run Sentiment analysis and LDA - topic detection on these tweets.
    Sentiment Analysis provides the tweets with negative contexts. On Analysis it was found that most of them are complaints.
    Running LDA on these gives us the topics about which most of the complaints are. Eg. water, late trains etc.
    
Assuming k=50 topics for LDA about complaints, we get the following terms in most of the topics :

train	  47 (8.3%)
coach	  23 (4.1%)
sir	    21 (3.7%)
pnr	    18 (3.2%)
help	  17 (3%)
ticket	15 (2.7%)
water	  13 (2.3%)
railway	10 (1.8%)
late	  9 (1.6%)
ac	    8 (1.4%)
station	8 (1.4%)
tatkal	7 (1.2%)

Clearly Indian railway needs to focus on Water facilities, Air conditioning of coaches and late running trains.

Sentiment Score Analysis:
It was interesting to see that out of approx. 2000 tweets, 1400 were negative ! Some examples just for an intuition are :
________ ______________________________________________________________________________________________________________________________________________
| label |	Tweet                                                                                                                                        |
| neg	  | @RailMinIndia @sureshpprabhu  dhauli worst train.12822 coach C1 ac not wrkng. refund money .why is this coach even there when ac nt working? |
| neg	  | @RailMinIndia confusion or misprint #whatever# but Chd to allp was worst noAC,ntClean,leaking in rain,noWater https://t.co/MLRJygEHmt        |
| neg	  | @RailMinIndia sir I am since morning and two time I had connected the at no 011-39340000 . But they give me very bad response . 1/2          |
------------------------------------------------------------------------------------------------------------------------------------------------------


2 images have been included for further understanding : 
1. Topic distribution
2. Sentiment Score distribution

Challenges : 
Hinglish and Hindi Tweets. Most of the sentiment analysis tools have been trained on English text, and to get correct
Sentiments for hindi and hinglish tweets is not possible.
