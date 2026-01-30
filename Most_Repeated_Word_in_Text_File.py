# importing Counter function
from collections import Counter

# input text file
inputFile = "text1.txt"

# Storing all the words
newWordsList = []

# Opening the given file in read-only mode
with open(inputFile, 'r') as filedata:

   # Traverse in each line of the file
   for textline in filedata:

      # Splitting the text file content into list of words
      wordsList = textline.split()

      # Traverse in the above list of words
      for word in wordsList:

         # Appending each word to the new list
         newWordsList.append(word)

# Using the Counter() function, calculate the frequency of all the words
wordsFrequency = Counter(newWordsList)

# Taking a variable to store the maximum frequency value
maxFrequency = 0

# Loop in the above words frequency dictionary
for textword in wordsFrequency:

   # Checking whether the frequency of the word is greater than the maximum frequency
   if(wordsFrequency[textword] > maxFrequency):
 
      # If it is true then set maximum frequency to the corresponding frequency value of the word
      maxFrequency = wordsFrequency[textword]

      # As this is the word with maximum frequency store this word in a variable
      mostRepeatedWord = textword

# Printing the most repeated word in a text file
print("{",mostRepeatedWord,"} is the most repeated word in a text file")

# Closing the input file
filedata.close()

# Printing the maximum frequency value
print("The maximum frequency is:",maxFrequency)

# Alternative approach using the most_common() method of Counter class
most_common_word = wordsFrequency.most_common(1)[0]
print(f"\nUsing most_common() method: '{most_common_word[0]}' is the most repeated word with a frequency of {most_common_word[1]}")

"""
# Another alternative approach using collections.Counter to find the most repeated word in a text file.
from collections import Counter

inputFile = "text1.txt"

newWordsList = []
with open(inputFile, "r") as filedata:
    for textline in filedata:
        newWordsList.extend(textline.split())

wordsFrequency = Counter(newWordsList)

mostRepeatedWord, freq = wordsFrequency.most_common(1)[0]
print(f"{{{mostRepeatedWord}}} is the most repeated word with frequency {freq}")
"""
