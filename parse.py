import sys
import parser

url = ''
target = ''

if __name__ == "__main__":

    try:
        url = sys.argv[1]
        target = sys.argv[2]
    except IndexError:
        print ("Improper number of arguments: usage is 'python parse.py <url> <target_string>'")
        exit(1)

    parser = parser.Parser()
    count = parser.parse(url, target)
    print("Target = %s, Count = %d" % (target, count))
