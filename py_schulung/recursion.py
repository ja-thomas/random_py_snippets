def nfind(haystack, needle, n, pos=0):
    pos = haystack.find(needle, pos)
    return pos if pos == -1 or n == 1 else nfind(haystack, needle, n-1, pos+1)

if __name__ == "__main__":
    hay = "asdf asdf 1234 asdf asfd"
    word = "asdf"
    res = nfind(hay, word, 2)
    print(res)