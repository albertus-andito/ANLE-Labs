import collections
import matplotlib.pyplot as plt
import sys

if __name__ == "__main__":
    num_of_lines = 0
    num_of_words = 0
    num_of_chars = 0

    with open(sys.argv[1], 'r') as file:
        for line in file:
            line = line.strip('\n')
            words = line.split()
            num_of_lines += 1
            num_of_words += len(words)
            num_of_chars += len(line)

    print('Number of lines in text file: ', num_of_lines)
    print('Number of words in text file: ', num_of_words)
    print('Number of characters in text file: ', num_of_chars)
    print('Average length of a word: ', round(num_of_chars / num_of_words, 2))

    file = open(sys.argv[1], 'r')
    all_chars = file.read().replace('\n', '').replace(' ', '').lower()
    all_chars = ''.join([c for c in all_chars if c.isalpha()])
    print('Most frequently occurring character: ', collections.Counter(all_chars).most_common(1))

    freq = collections.Counter(all_chars).most_common()
    print(freq)
    freq_alpha = [fr[0] for fr in freq]
    freq_freq = [fr[1] for fr in freq]
    plt.bar(freq_alpha, freq_freq)

    plt.show()
