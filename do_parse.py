#!/usr/bin/env python
"""
HTML parser, used for command-line testing and execution
Calls parser.parse for the main return
Usage::
    ./do_parse.py <url_string> <target_word>
Return::
    "Target = <target_word>, Count = <count>"
"""
import sys
import parser

url = ''
target = ''

if __name__ == "__main__":

    try:
        url = sys.argv[1]
        target = sys.argv[2]
    except IndexError:
        print ("Improper number of arguments: usage is 'python do_parse.py <url> <target_string>'")
        exit(1)

    parser = parser.Parser()
    count = parser.parse(url, target)
    print("Target = %s, Count = %d" % (target, count))
