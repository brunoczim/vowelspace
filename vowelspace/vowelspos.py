import csv
import sys
from vowelspace.cardinals import make_backness_fn, make_height_fn
from vowelspace.diagram import Vowel
from vowelspace.fmt import show_float

def main():
    backness_fn = make_backness_fn()
    height_fn = make_height_fn()
    reader = csv.reader(sys.stdin)
    writer = csv.writer(sys.stdout)

    for row in reader:
        if len(row) != 4:
            print("Expected row length to be 4", file=sys.stderr)
            sys.exit(1)

        try:
            f1 = float(row[1])
            f2 = float(row[2])
            roundedness = float(row[3])
        except ValueError as err:
            print(err, file=sys.stderr)
            sys.exit(1)

        backness = backness_fn(f1, f2, roundedness)
        height = height_fn(f1, f2, roundedness)
        x, y = Vowel(backness=backness, height=height).pos()
        writer.writerow([row[0], show_float(x), show_float(y)])
