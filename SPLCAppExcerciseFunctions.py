# Title: Data Exercise for SPLC Canidates (Functions).
# Description: Includes the functions i wrote to support the main exercise program. Moved functions here for cleaner code.
# Written by: Kingsley Bawuah
# Date: 06/24/18
from urllib.request import urlopen as uRequest  # Importing HTML client
from bs4 import BeautifulSoup as parser  # Importing Parsing Library.
import nltk  # Importing Natural Language Toolkit
from nltk.tokenize import RegexpTokenizer  # Importing tokenizer
from collections import Counter  # Importing Counter library.



# Function Name : wordCountDisplay
# Function Parameters : List of tokens
# Function Description : This function displays the number of elements in a list
# Function Returns: Nothing.
def wordCountDisplay(tokenList):
    print("The number of words for this article: ")
    print(len(tokenList))


# Function Name : scrapensave
# Function Parameters : myUrl,num
# Function Description : This function connects, scrapes, and saves a webpage.
# Function Returns: Returns the scraped data in lowercase format.
def scrapensave(myUrl, num, num2=0):
    # Open connection to the web-page, read, and close.
    uClient = uRequest(myUrl)
    pageHtml = uClient.read()
    uClient.close()

    # HTML "page soup" is stored here.
    page_soup = parser(pageHtml, "html.parser")
    if num2:
        text = page_soup.find("div",
                              {
                                  "class": "field field-name-body field-type-text-with-summary field-label-above"}).getText()[
               num:num2]
    else:
        text = page_soup.find("div",
                              {
                                  "class": "field field-name-body field-type-text-with-summary field-label-above"}).getText()[
               num:]

    # Return text in lowered form for uniformity when doing calculations.
    return text.lower()


# Function Name : removeStopWords
# Function Parameters : List of tokens from text.
# Function Description : This function will remove the english stop words from a list of tokens.
# Function Returns: The list without the stop words included.
def removeStopWords(tokenList):
    eStopWords = nltk.corpus.stopwords.words('english')
    newTokenList = []
    for token in tokenList:
        if token not in eStopWords:
            newTokenList.append(token)
    return newTokenList


# Function Name : tokenizerList
# Function Parameters : String of text from a web-page
# Function Description : Parses a string into tokens (A.k.a a list of words)
# Function Returns: The list of tokens
def tokenizerList(string):
    # Using the regex for all words, NOTE/ISSUE: this will cause hyphenated words to be seperated and the hyphen ignored.
    # Wasn't sure on the specifications for this.
    tokenizer = RegexpTokenizer("([A-Za-z0-9-']+)")

    tokens = tokenizer.tokenize(string)

    return tokens


# Function Name : plotFrequencies
# Function Parameters : listofTokens and a title for the graph
# Function Description : This function, graphs the frequency distribution of words in a set of tokenized data.
# Function Returns : Nothing, a graph is displayed.
def plotFrequencies(listofTokens, title):
    listofTokens = removeStopWords(listofTokens)
    frequencyDist = nltk.FreqDist(listofTokens)
    frequencyDist.plot(10, title=title, color="green",
                       linewidth='10')


# Function Name : displayCommon3
# Function Parameters : List of tokenized text
# Function Description : This function prints the top 3 most common words in a profile.
# Function Returns : Nothing
def displayCommon3(listofTokens):
    listofTokens = removeStopWords(listofTokens)
    frequencyDist = nltk.FreqDist(listofTokens)
    frequencyDist = dict(Counter(frequencyDist).most_common(3))
    # Now for each value in the sorted dictionary lets print.
    print("The three most common values used in this Extremist profile are: ")
    for word, count in frequencyDist.items():
        print(word)


# Function Name : displayshared3
# Function Parameters : 2 Different lists of tokenized text
# Function Description : This function prints the top 3 most common words shared between two profiles.
# Function Returns : Nothing
def displayshared3(listofTokens, listofTokens2):
    listofTokens = removeStopWords(listofTokens)
    listofTokens2 = removeStopWords(listofTokens2)

    frequencyDist = nltk.FreqDist(listofTokens)
    frequencyDist2 = nltk.FreqDist(listofTokens2)

    freqIntersect = {}

    allKeys = set(list(frequencyDist.keys()) + list(frequencyDist2.keys()))

    for key in allKeys:
        if key in frequencyDist and key in frequencyDist2:
            freqIntersect[key] = frequencyDist[key] + frequencyDist2[key]

    freqIntersect = dict(Counter(freqIntersect).most_common(3))

    print("The three most common values used in both Extremist profiles are: ")
    for word, count in freqIntersect.items():
        print(word)
