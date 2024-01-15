# Importing the required libraries
import nltk
from nltk.corpus import opinion_lexicon

# Loading the positive and negative word lists
positive_words = set(opinion_lexicon.positive())
negative_words = set(opinion_lexicon.negative())

# Classifying the words
text = "Nice weather today I will go out for having fun with my freinds, we will return home before night ugly beautiful bad good nice horrible"
words = nltk.word_tokenize(text)
positive_count = 0
negative_count = 0
for word in words:
    if word in positive_words:
        positive_count += 1
        #print("total positive", positive_count)
    elif word in negative_words:
        negative_count += 1
       # print("total negative", negative_count)
print("total positive", positive_count)
print("total negative", negative_count)
# Printing the results
if positive_count > negative_count:
    print("The text is positive.")
elif positive_count < negative_count:
    print("The text is negative.")
else:
    print("The text is neutral.")
