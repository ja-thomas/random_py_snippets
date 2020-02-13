def haystack_gen(haystack, needle):
    pos = haystack.find(needle, 0)
    while pos != -1:
        yield pos
        pos = haystack.find(needle, pos+1)

if __name__ == "__main__":
    hay = "asdf asdf 123 asdf asdf"
    need = "asdf"

    for p in haystack_gen(hay, need):
        print(p)

    c = [4.2, 5.2, 1.2]
    map(lambda x: 9 * x / 5 + 32, c)