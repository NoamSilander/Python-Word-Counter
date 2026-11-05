def text_cleaner(file):
    with open(file, encoding='utf-8') as f:
        words_clean = []
        for line in f:
            words = line.split()
            for word in words:
                clean_word = ''
                for char in word:
                    if char.isalpha():
                        clean_word += char.lower()
                words_clean.append(clean_word)
    return words_clean

word_counter('text.txt')