import sys
import os

def load(file):
    """Open a text file & return a list of lowercase strings"""
    try:
        with open(os.path.join(sys.path[0], file)) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file = sys.stderr)
        sys.exit