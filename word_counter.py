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

def word_counter(words):
    word_dict = {}
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        elif word in word_dict:
            word_dict[word] += 1
    return word_dict


def main(file):
    words = text_cleaner(file)
    word_dict = word_counter(words)
    for word, count in word_dict.items():
         print(f'{word}: {count}')


if __name__ == '__main__':
    main('text.txt')