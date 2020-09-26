# -----------------------------------------------------------------------------
# Name:        wordstats
# Purpose:     to read and analyze a large text file
#
# Author:       Michal Golovanevsky
# Date:         07/17/17
# -----------------------------------------------------------------------------
"""
The program opens and reads a very large text file

The program prompts the user to enter the file name.

The program then computes: the longest word used in the file, the five most
common words in the file with the number of times, they appear in the file,
and the word count of all the words in the file, sorted alphabetically.
"""
import string
# The following imports are needed for the draw_cloud function.
import tkinter
import tkinter.font
import random


# The draw_cloud function is only needed for the optional part:
# to generate a word cloud.
def draw_cloud(input_count, min_length=0):
    """
    Generate a word cloud based on the input count dictionary specified.

    Parameters:
    input_count (dict): represents words and their corresponding counts.
    min_length (int):  optional - defaults to 0.
         minimum length of the words that will appear
         in the cloud representation.
    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """
    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
        word: input_count[word] for word in input_count
        if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame = tkinter.Frame(root)
    frame.grid()
    my_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[0:20]:
        color = '#' + str(hex(random.randint(256, 4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word] * ratio))
        label = tkinter.Label(frame, text=word, font=word_font, fg=color)
        label.grid(row=my_row % 5, column=my_row // 5)
        my_row += 1
    root.mainloop()


def get_input():
    """
    Prompts the user for a file name

    Parameters: none
    Returns: the user's input filename (file)
    """
    filename = input('Please enter a file name: ')
    return filename

def count_words(filename):
    """
    builds and return the dictionary for the given filename

    Parameters: filename (file)
    Returns: words_dict (dictionary) with all the words in the file and the
    amount of times each appears
    """
    words_dict = {} # initializes the dictionary
    with open(filename, 'r', encoding='utf-8') as file: # reads the file
        for line in file:
            line = line.lower()  # converts the line to lower case
            for word in line.split(): # splits the line into words
                word = word.strip(string.punctuation + string.digits
                + string.whitespace) # takes out special characters
                if word:
                    if word not in words_dict: # if word isn't already in dict
                        words_dict[word] = 1 # initializes value to the word
                    else:
                        words_dict[word] +=1 # adds 1 when word appears again
    return words_dict


def report(word_dict):
    """
    reports on various statistics based on the given word count dictionary
    writes to out.txt file

    Parameters: word_dict (dictionary)
    Returns: none

    """
    words = sorted(word_dict, key=len) # stores sorted dictionary
    longest_word = max(words, key=len) # finds longest word
    print('The longest word is: ', longest_word)

    # sorts dictionary from largest to smallest value
    most_common_words = sorted(word_dict, key=word_dict.get,reverse=True)
    print('The 5 most common words are:')
    my_list = most_common_words[0:5] # saves only the largest 5 values
    for word in my_list:
        print(word + ':', word_dict[word])

    # writes to out.txt file
    with open('out.txt', 'w', encoding='utf-8') as my_file:
        for word in sorted(word_dict):  # print letters in alphabetical order
           my_file.write(word + ': ' + str(word_dict[word]) + '\n')

def main():
    filename = get_input() # get the input filename and save it in a variable
    # call count_words to build the dictionary for the given file
    word_dict = count_words(filename)
    word_count = word_dict # save the dictionary in the variable word_count
    # call report to report on the contents of the dictionary word_count
    report(word_count)
    draw_cloud(word_count)


if __name__ == '__main__':
    main()
