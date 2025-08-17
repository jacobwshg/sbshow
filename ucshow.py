from sys import argv

# show character codepoint
def uc_showc(c):
    return f'{c}\t{hex(ord(c))}'

# show string codepoints
def uc_shows(s):
    return '\n'.join([uc_showc(c) for c in s])

USAGE = 'Usage: ucshow.py <str1> (<str2> ...)'

# forgot this is Python
def main():
    if len(argv) <= 1:
        print(USAGE)
        exit()
    for s in argv[1:]:
        print(f'{uc_shows(s)}\n')
    exit()

if __name__ == '__main__':
    main()

