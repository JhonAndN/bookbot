path_to_file = 'C:/Users/dzoni/workspace/github.com/bookbot/bookbot/books/frankenstein.txt'

def Print(Text):
    print(Text)

def ReadFile():
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def CountWords(Text):
    print(len(Text.split()))

def Count_Letters(Text):
    Counted = {}
    for c in Text:
        if c.lower() in Counted:
            Counted[c.lower()] += 1
        else:
            Counted[c.lower()] = 1
    print(Counted)
       

def main():
    AllText = ReadFile()
    CountWords(AllText)
    Count_Letters(AllText)

if __name__ == '__main__':
    main()

#"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"