def find_needle(haystack):
    a = haystack.index('needle')
    return f"found the needle at position {a}"


if __name__ == "__main__":
    print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))


"""

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"

"""