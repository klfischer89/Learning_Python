# Morse code dictionary
morse = {
    "a" : ".-", 
    "b" : "-...", 
    "c" : "-.-.", 
    "d" : "-..", 
    "e" : ".", 
    "f" : "..-.", 
    "g" : "--.", 
    "h" : "....", 
    "i" : "..", 
    "j" : ".---", 
    "k" : "-.-", 
    "l" : ".-..", 
    "m" : "--", 
    "n" : "-.", 
    "o" : "---", 
    "p" : ".--.", 
    "q" : "--.-", 
    "r" : ".-.", 
    "s" : "...", 
    "t" : "-", 
    "u" : "..-", 
    "v" : "...-", 
    "w" : ".--", 
    "x" : "-..-", 
    "y" : "-.--", 
    "z" : "--..", 
    "0" : "-----", 
    "1" : ".----", 
    "2" : "..---", 
    "3" : "...--", 
    "4" : "....-", 
    "5" : ".....", 
    "6" : "-....", 
    "7" : "--...", 
    "8" : "---..", 
    "9" : "----.", 
    "." : ".-.-.-", 
    "," : "--..--",
    "?" : "--..--",
    "ä" : ".-.-",
    "ö" : "---.",
    "ü" : "..__",
    "ß" : "...__..",
    " " : " "
}

text = "Jeder wackere Bayer vertilgt bequem zwo Pfund Kalbshaxen"  # sample text
text = text.lower()  # convert to lowercase
morse_code = ""  # initialize empty string for morse code
for char in text:  # iterate through each character in the text
    if char in morse:  # check if character is in morse dictionary
        morse_code += morse[char] + " "  # append morse code and a space
    else:
        morse_code += "? "  # append '?' for unknown characters 

print(morse_code)  # print the final morse code string
# Example output:
# .--- . -.. . .-.  .-- .- -.-. -.-

text = "the quick brown fox jumps over the lazy dog" # sample text

# English to German and German to French dictionaries
en_de = {
    "the" : "der",
    "quick" : "schnell",
    "brown" : "braun",
    "fox" : "fuchs",
    "jumps" : "springt",
    "over" : "über",
    "lazy" : "faul",
    "dog" : "hund"
}

de_fr = {
    "der" : "le",
    "schnell" : "rapide",
    "braun" : "brune",
    "fuchs" : "renard",
    "springt" : "claque",
    "über" : "par",
    "faul" : "pourri",
    "hund" : "chien"
}

words = text.split()  # split text into words

# Translate from English to German
german_translation = ""
for word in words:
    if word in en_de:
        german_translation += en_de[word] + " "
    else:
        german_translation += "? "  # unknown word
print("German Translation:", german_translation.strip())

# Translate from German to French
german_words = german_translation.strip().split() # split German translation into words
french_translation = "" # initialize empty string for French translation
# Translate from German to French
for word in german_words:
    if word in de_fr:
        french_translation += de_fr[word] + " "
    else:
        french_translation += "? "  # unknown word
print("French Translation:", french_translation.strip())
