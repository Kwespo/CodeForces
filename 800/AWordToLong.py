"""
Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

Let's consider a word too long, if its length is strictly more 
than 10 characters. All too long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the 
last letter of a word and between them we write the number of letters between the first and the last letters. 
That number is in decimal system and doesn't contain any leading zeroes.

Thus, "localization" will be spelt as "l10n", and "internationalization» 
will be spelt as "i18n".

You are suggested to automatize the process of changing the words with 
abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

Input
The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n 
lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.
"""
n = int(input())#How many numbers there will be

for i in range(0, n): #Loops for the amount there is
  word = input() #input the word
  if len(word) > 10: #if the word is smaller then 10 then it will not be abriviated
    print(word[0] + str((len(word) - 2)) + word[len(word)-1]) #prints out the words first and last letter and the length
  else: print(word) #prints the word without and edits if under 10 letters