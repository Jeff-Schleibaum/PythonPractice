#jeff schleibaum
# write a function that counts how many vowels are in a string

def vowel_count(word):
        vowels= "a", "e", "i", "o", "u" # declare vowels
        count= 0 # declare count starting at zero
        for letter in word: # create variable name letter in word
            if letter in vowels: # check if letter is a vowel
                count += 1 # increase count if letter is a vowel

        return count


print(vowel_count("computer"))
print(vowel_count("place"))
print(vowel_count("python"))