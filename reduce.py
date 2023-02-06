import sys

# using a dictionary to map words to their counts
current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    # output: indonesia    1

    # split input string to 2 vars by tab
    word, count = line.split('\t', 1)
    # word = indonesia
    # count = 1

    # convert to integer for summary step
    try:
        count = int(count)
        # count = 1 as integer
    except ValueError:
        continue

    # checking antara current word dan word
    if current_word == word:
        # brazil == brazil
        current_count += count
        # current_count = 3
    else:
        # step ini tidak akan berjalan ketika current_word = None
        if current_word:
            print('%s\t%s' % (current_word, current_count))
            # brazil    3

            current_count = count
            # current_count = 1
            current_word = word
            # current_word = indonesia
        else:
            current_count = count
            # current_count = 1
            current_word = word
            # current_word = Brazil

if current_word == word:
    print('%s\t%s' % (current_word, current_count))
