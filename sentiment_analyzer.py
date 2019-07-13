# VADER is a sentiment analysis tool
# import SentimentIntensityAnalyser class
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# this is the main function printing the sentiments of the sentence
def sentiment_score(sentence):
    # create the SentimentIntensityAnalyser object
    obj = SentimentIntensityAnalyzer()
    # polarity_scores method of this object gives a sentiment dictionary which contains pos, neg, neu and compound scores
    sentiment_dict = obj.polarity_scores(sentence)
    print("Overall sentiment dictinary is: ", sentiment_dict)
    print("Sentence is ", sentiment_dict['neg']*100, " % negative")
    print("Sentence is ", sentiment_dict['pos']*100, " % positive")
    print("Sentence is ", sentiment_dict['neu']*100, " % neutral")
    print("Sentence overall rated as ")

    # decide if sentence is positive, negative or neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
    elif sentiment_dict['compound'] <= -0.05 :
        print("Negative")
    else :
        print("Neutral")



# driver code
if __name__=="__main__":
    print("1st statement:\n")
    sentence = "I am very excited for this!"
    print(sentence)
    # function call
    sentiment_score(sentence)

    print("\n2nd statement:\n")
    sentence = "Studies are going on as usual"
    print(sentence)
    # function call
    sentiment_score(sentence)

    print("\n3rd statement:\n")
    sentence = "I am very sad"
    print(sentence)
    # function call
    sentiment_score(sentence)
