from sys import argv

# show bytes in character
def cbshow(c):
    return f'{c}\t{hex(ord(c))}'

# show bytes in string
def sbshow(s):
    return '\n'.join([cbshow(c) for c in s])

# forgot this is Python
def main():
    for s in argv[1:]:
        print(f'{sbshow(s)}\n')
    exit()

if __name__ == '__main__':
    main()

