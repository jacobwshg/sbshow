from sys import argv

# show bytes in character
def cbshow(c):
    return f'{c}\t{hex(ord(c))}'

# show bytes in string
def sbshow(s):
    return '\n'.join([cbshow(c) for c in s])

USAGE = 'Usage: sbshow.py <str1> (<str2> ...)'

# forgot this is Python
def main():
    if len(argv) <= 1:
        print(USAGE)
        exit()
    for s in argv[1:]:
        print(f'{sbshow(s)}\n')
    exit()

if __name__ == '__main__':
    main()

