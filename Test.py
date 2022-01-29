word_without_vowels = ""
user_word = str(input("Enter your word please "))
user_word = user_word.upper()

for i in user_word:
   if i == "A" or i == "E" or i == "I" or i == "O" or i == "U": 
       word_without_vowels = word_without_vowels + i
       continue
   print(i)
print(word_without_vowels)
