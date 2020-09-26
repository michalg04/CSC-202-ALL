# -----------------------------------------------------------------------------
# Name:        aggregator.py
# Purpose:     CS 21A - implement a simple general purpose aggregator
#
# Author:       Michal Golovanevsky
# -----------------------------------------------------------------------------
"""
Implement a simple general purpose aggregator

Usage: aggregator.py filename topic
filename: input  file that contains a list of the online sources (urls).
topic:  topic to be researched and reported on
"""

import urllib.request
import urllib.error
import re
import sys
import textwrap


def aggregator(filename, topic):
    """
    Searches for topic in a set of urls listed in filename
    Generates an output file containing the url and the text
    associated with the topic

    Parameters: filename (string) and topic (string)
    Returns: none

    """
    pattern = r'>([^<]*\b{}\b[^>]*?)<'.format(topic)
    name = topic + 'summary.txt'
    delimiter = 25 * "-"
    try:
        with open(filename, 'r', encoding='utf-8') as in_file:
            with open(name, 'w', encoding='utf-8') as out_file:
                for line in in_file:
                    try:
                        with urllib.request.urlopen(line) as url_file:
                            page = url_file.read()
                            try:
                                decoded_page = page.decode('UTF-8')
                                matches = re.findall(pattern, decoded_page,
                                                 re.IGNORECASE | re.DOTALL)
                                if matches:
                                    lline = textwrap.wrap(line, 75)
                                    l = '\n'.join(lline)
                                    out_file.write('Source\n' + 'url:'
                                                   + l + '\n\n')
                                    for match in matches:
                                        mmatch = textwrap.wrap(match,79)
                                        m = '\n'.join(mmatch)
                                        out_file.write('{}\n'.format(m))
                                    out_file.write(delimiter + '\n\n')
                            except UnicodeDecodeError as decode_err:
                                print('Error decoding url: ', line, decode_err)
                    except urllib.error.URLError as url_err:
                        print('Error opening url: ', line, url_err)
    except:   # all other cases
        print('Unexpected error')


def get_arguments(args):
    """
    Recieves sys.argv and generates and error if the number of arguments
    is invalid

    Parameters: arg (list of strings)
    Returns: filename (string) and topic (string)

    """
    filename = ''
    topic = ''

    if len(args) != 3:  # Check for the right number of arguments
        print ('Error:  invalid number of arguments')
        print('Usage: aggregator.py filename topic')
    else:
        filename = args[1]  # Get the name argument
        topic = args[2]  # Get the number argument
    return (filename, topic)


def main():
    (filename, topic) = get_arguments(sys.argv)
    if filename and topic:
        aggregator(filename, topic)

if __name__ == '__main__':
    main()