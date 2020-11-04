# Create empty dict to store keys (words) and their values(counts)
histogram = dict()

# Open, read, make lowercase, strip of whitespaces
with open(r"D:\myDifferent\Python Code\stepik_67\dataset_3363_3.txt", 'r') as fh:

    for line in fh:
        line = line.lower().strip()

        # Split into separate words by space
        for word in line.split():
            # If key in dict, increment counter (value) by 1
            # Else add new key with default value 0 and increment by 1
            histogram[word] = histogram.get(word, 0) + 1

# List to store keys (words) with equal maximum count
# Counter to keep track of the largest value so far
max_words = []
max_count = 0

# Traverse the dictionary keys, compare values and remember the key with greatest value
for w in histogram.keys():

    # If the value of current key greater than current maximum:
    # update max_count
    # clear the possibly non-empty list max_words
    # add current key to the max_words list
    if histogram[w] > max_count:
        max_count = histogram[w]
        max_words = []
        max_words += [w]
    # Else if the value of current key is equal to current maximum:
    # Ad current key to the max_words list
    #

    elif histogram[w] == max_count:
        max_words += [w]

# Sort the max_words list lexicographically
max_words.sort()

print(max_words[0], histogram[max_words[0]])
