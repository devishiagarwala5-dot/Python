import colorama 
from colorama import Fore, Style
from textblob import TextBlob
#textblob is a library used for sentiment analysis
colorama.init()
print(f"{Fore.BLUE}Welcome to my sentiment analysis")
print("Enter your name: ")
name=input()
print(f"{Fore.GREEN} WELCOME ", name)
feedback=input("What do you think about my store?")
polarity=TextBlob(feedback).sentiment.polarity
if polarity>0.25:
    sentiment_type="Positive"
    
elif polarity<-0.25:
    sentiment_type="Negative"

else:
    sentiment_type="Neutral"

print(f"Thankyou for your {sentiment_type} feedback")