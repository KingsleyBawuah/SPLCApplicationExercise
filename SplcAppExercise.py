# Title: Data Exercise for SPLC Canidates.
# Description: Scrapes text from two extremist profiles, counts total words, and plots the frequency of words mentioned.
# along with some calculation done in NLTK
# Written by: Kingsley Bawuah
# Date: 06/24/18
from SPLCAppExcerciseFunctions import scrapensave
from SPLCAppExcerciseFunctions import tokenizerList
from SPLCAppExcerciseFunctions import wordCountDisplay
from SPLCAppExcerciseFunctions import plotFrequencies
from SPLCAppExcerciseFunctions import displayCommon3
from SPLCAppExcerciseFunctions import displayshared3
import nltk

myUrl_1 = 'https://www.splcenter.org/fighting-hate/extremist-files/individual/mike-cernovich'
myUrl_2 = 'https://www.splcenter.org/fighting-hate/extremist-files/individual/andrew-anglin'
nltk.download('stopwords')

# Main
# First Profile + Graph
print("-----------------------MIKE CERNOVICH -- PROFILE INFORMATION------------------------ ")
data1 = scrapensave(myUrl_1, 11)
listofTokens = tokenizerList(data1)
wordCountDisplay(listofTokens)
plotFrequencies(listofTokens, "Word Frequencies in Mike Cernovich's Extremist Profile")
displayCommon3(listofTokens)

# Second Profile + Graph
print("--------------ANDREW ANGLIN -- PROFILE INFORMATION------------------- ")
data2 = scrapensave(myUrl_2, 10)
listofTokens2 = tokenizerList(data2)
wordCountDisplay(listofTokens2)
plotFrequencies(listofTokens2, "Word Frequencies in Andrew Anglin's Extremist Profile")
displayCommon3(listofTokens2)

# Most common values between both Profiles.
print("----------------SHARED PROFILE INFORMATION-------------")
displayshared3(listofTokens, listofTokens2)

# Most common words only in the section "In their own words"
# First Profile
print("----------------MIKE CERNOVICH -- PROFILE INFORMATION -- IN THEIR OWN WORDS SECTION--------------- ")
data1 = scrapensave(myUrl_1, 474, 2704)
listofTokens = tokenizerList(data1)
displayCommon3(listofTokens)

#Second Profile
print(" --------------ANDREW ANGLIN -- PROFILE INFORMATION-- IN THEIR OWN WORDS SECTION------------------ ")
data2 = scrapensave(myUrl_2, 264, 2360)
listofTokens2 = tokenizerList(data2)
displayCommon3(listofTokens2)