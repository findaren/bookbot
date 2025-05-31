def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read()
    except Exception as e:
        raise e
    return file_contents

def words_in(text):
    word_collection = {}
    try:
        word_collection = text.split()
        number_of_words = len(word_collection)
        return(number_of_words)
    except Exception as e:
        raise e
    
def character_summary(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts

def print_report(file):
    text=get_book_text(file)
    wc = words_in(text)
    characters=character_summary(text)
    char_sort = {key: value for key, value in sorted(characters.items(),key=lambda item: item[1],reverse=True)}    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for l in char_sort:
        print(f"{l}: {characters[l]}")
    print("============= END ===============")