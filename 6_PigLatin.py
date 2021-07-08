# This project translates English sentences to Pig Latin and Pig Latin to English

# These are the rules for Pig Latin
# If a word starts with a vowel, add ay to the end of it
# If a word starts with a single (orthographicallly) consonant, move that consonant
# to the end of the word and then add ay
# If a word starts with two consonants (orthographically) or more, move these consonants
# to the end of the word and then add ay
# Source: https://web.ics.purdue.edu/~morelanj/RAO/prepare2.html

# Packages needed
import sys
import time


# English to Pig 
def EngToPig():
    # Create list to store output
    translation = []
    vowels = ["e","u","i","o","a","y"]
    # Check whether there is any input at all
    language = input("Please input the phrase or phrases you'd like to translate\n").lower()
    if len(language) == 0:
        print("This phrase could not be translated")
    # Chunk output into words 
    language = language.split()
    # Check whether the input contains any special characters
    for word in language:
        if not word.isalpha():
            print("This word cannot be translated - please remove any special characters")
        else:
            # If the first item in a word is a vowel, translate according to piglatin
            if word[0] in vowels:
                word += "ay"
                translation.append(word)
            else:
                # Find the amount and type of consonants before the first vowel
                consonantLength = 0
                for letter in word:
                    if letter not in vowels:
                        consonantLength += 1
                    else:
                        break 
                frontConsonants = word[0:consonantLength]
                word = word[consonantLength:len(word)] + frontConsonants + "ay"
                translation.append(word)
    # If there is a translation, print it
    if len(translation) > 0:
        # Divide translation into words
        translation = " ".join(translation)
        print(translation)

    # check whether the first letter in a word is vowel
    # loop through each word that doesn't start with a vowel and then extract the string until it reaches a vowel
def PigLatinTranslate():
    wordstoQuit = ["exit","quit","stop"]
    # Check which language the user wants to translate from
    while True:
        languageType = input("Please indicate whether the phrase you typed is Pig Latin (P) or English (E)\n").lower()
        if languageType in wordstoQuit:
            sys.exit()
        elif languageType in ["P","p"]:
            time.sleep(0.5)
            print("It is not yet possible to translate from Pig Latin, please input your phrase in English")
            #PigToEng()- This is not possible for me right now, but it might be later
            PigLatinTranslate()
        elif languageType in ["E","e"]:
            time.sleep(0.5)
            print("You have selected English")
            EngToPig()
            PigLatinTranslate()
        else:
            print("You have selected neither")
            PigLatinTranslate()
PigLatinTranslate()

