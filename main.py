import string

def countWords(book):
    length = 0
    with open(book)as f:
        fileContents = f.read()
        words = fileContents.split()
      
    length = len(words)
    return length


def countEachChar(book):
    alphabet_dict = dict.fromkeys(string.ascii_lowercase, 0)
    with open(book)as f:
        fileContents = f.read()
    
    fileContents = fileContents.lower()

    for char in fileContents:
        if char in alphabet_dict:
            alphabet_dict[char] += 1

    return alphabet_dict


def main():
    BOOK = "books/frankenstein.txt"
    getWords = countWords(BOOK)
    alphabetCount = countEachChar(BOOK)
    print(f"--- Begin of the report for {BOOK} ---")
    print(f"{getWords} words found in the document")
    print(f"")
    for char in alphabetCount:
        print(f"The '{char}' character was found {alphabetCount[char]} times")
    print(f"--- End of report ---")

main ()

