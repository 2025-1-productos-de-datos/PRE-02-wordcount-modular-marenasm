# obtain a list of files in the input directory
import os

from ._internals.write_count_words import write_count_words


def red_all_lines():
    all_lines = []
    input_file_list = os.listdir("data/input/")
    for filename in os.listdir("data/input/"):
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines


def main():

    ###
    input_file_list = os.listdir("data/input/")
    # all_lines = red_all_lines()

    ## red all lines
    ## precrocess lines
    ## split in words
    ## count words
    ## write count words

    # count the frequency of the words in the files in the input directory
    counter = {}
    for filename in input_file_list:
        with open("data/input/" + filename) as f:
            for l in f:
                for w in l.split():
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1

    # create the directory output/ if it doesn't exist
    write_count_words(counter)


if __name__ == "__main__":
    main()
