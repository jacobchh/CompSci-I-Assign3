# Hello this is Jacob Chun
# Today is November 2, 2019
# The following program analyzes a tweet file and keywords file submitted by the user and performs sentiment analysis

# imports all functions that are used within the main function
from sentiment_analysis import compute_tweets


def main():
    # prompts user for the files that they would like to analyze
    tweetFile = input("Please enter the name of the tweet file you wish to process: ")
    keyFile = input("Please enter the name of the keyword file you wish to use: ")

    # takes the files and uses the function compute_tweets to return a list of values
    values = compute_tweets(tweetFile, keyFile)

    # takes the list of values and prints them in a readable fashion
    print("\nEastern Region Results")
    print("%-35s" % "Happiness score:", values[0][0],
          "\n%-35s" % "Number of keyword tweets:", values[0][1],
          "\n%-35s" % "Total number of tweets:", values[0][2])

    print("\nCentral Region Results")
    print("%-35s" % "Happiness score:", values[1][0],
          "\n%-35s" % "Number of keyword tweets:", values[1][1],
          "\n%-35s" % "Total number of tweets:", values[1][2])

    print("\nMountain Region Results")
    print("%-35s" % "Happiness score:", values[2][0],
          "\n%-35s" % "Number of keyword tweets:", values[2][1],
          "\n%-35s" % "Total number of tweets:", values[2][2])

    print("\nPacific Region Results")
    print("%-35s" % "Happiness score:", values[3][0],
          "\n%-35s" % "Number of keyword tweets:", values[3][1],
          "\n%-35s" % "Total number of tweets:", values[3][2])


# calls the main function
main()
