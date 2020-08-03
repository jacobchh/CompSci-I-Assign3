# Hello this is Jacob Chun
# Today is November 2, 2019
# The following file contains a function compute_tweets which takes a tweet file and analyzes it
# It will compare the tweets to a key word file to calculate the sentiment score
# Furthermore, it will sort the sentiment score based on location of the tweet

# imports punctuation variable used later on
from string import punctuation


def compute_tweets(tweets, keywords):
    # defines some variables used later on
    blankList = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
    keyList = []
    easternTotal = 0
    centralTotal = 0
    mountainTotal = 0
    pacificTotal = 0
    easternKeyTotal = 0
    centralKeyTotal = 0
    mountainKeyTotal = 0
    pacificKeyTotal = 0
    easternScore = 0
    centralScore = 0
    mountainScore = 0
    pacificScore = 0

    # try loop in case of errors that the program may encounter
    try:
        tweetFile = open(tweets, "r", encoding="utf-8")
        keywordFile = open(keywords, "r", encoding="utf-8")

        # processes the selected keyword file and turns it to a list
        for line in keywordFile:
            for element in processKeyFile(line):
                keyList.append(element)

        # large loop for processing the entire tweet file
        for line in tweetFile:

            # if there is an empty line it will skip the line
            if line == "" or line == "\n":
                continue

            # returns a list comprised of one single tweet
            tweetList = formatLine(line)

            # finds the region the tweet is located in and returns the region name
            region = findRegion(tweetList)

            # calculates the score of a single tweet based on the keyList given
            # totals the tweets of a region, key tweets of a region, and score of a region
            # if the score of the line is not zero, it will add '1' to the key tweet total
            if region == "Eastern":
                easternTotal = easternTotal + 1
                if calculateScore(tweetList, keyList) != 0:
                    easternKeyTotal = easternKeyTotal + 1
                    easternScore = easternScore + calculateScore(tweetList, keyList)

            elif region == "Central":
                centralTotal = centralTotal + 1
                if calculateScore(tweetList, keyList) != 0:
                    centralKeyTotal = centralKeyTotal + 1
                    centralScore = centralScore + calculateScore(tweetList, keyList)

            elif region == "Mountain":
                mountainTotal = mountainTotal + 1
                if calculateScore(tweetList, keyList) != 0:
                    mountainKeyTotal = mountainKeyTotal + 1
                    mountainScore = mountainScore + calculateScore(tweetList, keyList)

            elif region == "Pacific":
                pacificTotal = pacificTotal + 1
                if calculateScore(tweetList, keyList) != 0:
                    pacificKeyTotal = pacificKeyTotal + 1
                    pacificScore = pacificScore + calculateScore(tweetList, keyList)

        # avoids a division by zero error if the tweet file has no key tweets for that region
        # calculates each region's score
        if easternKeyTotal != 0:
            easternScore = easternScore / easternKeyTotal
        if centralKeyTotal != 0:
            centralScore = centralScore / centralKeyTotal
        if mountainKeyTotal != 0:
            mountainScore = mountainScore / mountainKeyTotal
        if pacificKeyTotal != 0:
            pacificScore = pacificScore / pacificKeyTotal

        # returns all values calculated in a list that can be used when the function is called
        totalValues = [(easternScore, easternKeyTotal, easternTotal),
                       (centralScore, centralKeyTotal, centralTotal),
                       (mountainScore, mountainKeyTotal, mountainTotal),
                       (pacificScore, pacificKeyTotal, pacificTotal)]

        # closes the tweet file open
        tweetFile.close()
        # closes the keyword file open
        keywordFile.close()

        return totalValues

    # handles the error of an invalid file name
    except IOError:
        print("\nError: File not found.")
        return blankList

    # handles the error of an unreadable file
    except ValueError:
        print("\nError: Invalid file or format not correct.")
        return blankList

    # handles the error of an unreadable file
    except IndexError:
        print("\nError: Invalid file or format not correct.")
        return blankList

    except RuntimeError as error:
        print("\nError:", str(error))
        return blankList


def processKeyFile(line):
    line = line.strip()
    tempList = line.split(",")
    return tempList


def formatLine(line):
    tweetList = line.split()

    # removes punctuation from coordinates and converts them to floats for calculation purposes
    for i in range(0, 2):
        tweetList[i] = tweetList[i].strip("[],")
    tweetList[0] = float(tweetList[0])
    tweetList[1] = float(tweetList[1])

    # removes punctuation and puts all words in lower case
    for i in range(2, len(tweetList)):
        tweetList[i] = tweetList[i].lower().strip(punctuation)

    return tweetList


def findRegion(tweetList):
    # coordinate value constants
    P1 = [49.189787, -67.444574]
    P2 = [24.660845, -67.444574]
    P3 = [49.189787, -87.518395]
    P5 = [49.189787, -101.998892]
    P7 = [49.189787, -115.236428]
    P9 = [49.189787, -125.242264]
    P10 = [24.660845, -125.242264]

    # defines variable used in the function
    region = ""

    # finds the region that the tweet is located in
    if P1[0] >= tweetList[0] >= P2[0] and P1[1] >= tweetList[1] >= P10[1]:
        if P1[1] >= tweetList[1] > P3[1]:
            region = "Eastern"
        elif P3[1] > tweetList[1] > P5[1]:
            region = "Central"
        elif P5[1] > tweetList[1] > P7[1]:
            region = "Mountain"
        elif P7[1] > tweetList[1] >= P9[1]:
            region = "Pacific"
    return region


def calculateScore(tweetList, keyList):
    # defines variables that are used in the calculation
    score = 0
    count = 0

    # loop starts at the very first element that is a word from the tweet
    for i in range(5, len(tweetList)):

        # checks to see if the element is all letters or else it may match to a number in keyList
        if tweetList[i].isalpha() and tweetList[i] in keyList:
            position = keyList.index(tweetList[i])
            score = score + int(keyList[position + 1])
            count = count + 1

    # avoids a division by zero error if the line has no key words
    if score != 0:
        return score / count
    else:
        return score
