"""
linear_classifier.py
Usage: python3 linear_classifier.py data_file.csv
"""

import csv, sys, random, math


def read_data(filename, delimiter=",", has_header=True):
    """Reads data from filename. The optional parameters can allow it
    to read data in different formats. Returns a list of headers and a
    list of lists of data."""
    data = []
    header = []
    with open(filename) as f:
        reader = csv.reader(f, delimiter=delimiter)
        if has_header:
            header = next(reader, None)
        for line in reader:
            example = [float(x) for x in line]
            data.append(example)

        return header, data

def convert_data_to_pairs(data):
    """Turns a data list of lists into a list of (attribute, target) pairs."""
    pairs = []
    for example in data:
        pair = (example[:-1], example[-1])
        pairs.append(pair)
    return pairs



def linear_classification_hard_threshold(training):
    """This is what you need to implement (and the logistic version)"""
    pass




def main():
    # Read data from the file provided at command line
    header, data = read_data(sys.argv[1], ",")

    # Convert data into (x, y) tuples
    example_pairs = convert_data_to_pairs(data)

    # Insert 1.0 as first element of each x to work with the dummy weight
    training = [([1.0] + x, y) for (x, y) in example_pairs]

    # See what the data looks like
    for (x, y) in training:
        print("x = {}, y = {}".format(x, y))

    # Run linear classification. This is what you need to implement
    w = linear_classification_hard_threshold(training)

if __name__ == "__main__":
    main()
