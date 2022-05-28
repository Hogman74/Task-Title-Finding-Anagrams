def find_anagram(word, anagram):
# [assignment] Add your code here
word = "please"
anagram = "places"

# check the length of wrods
if (len(word) == len(anagram)):
# sort the strings
sorted_word = sorted(word)
sorted_anagram= sorted(anagram)

# if sorted arrays are the same
if (sorted_word == sorted_anagram):
return True
else:
return False

print(find_anagram("please", "places"))
