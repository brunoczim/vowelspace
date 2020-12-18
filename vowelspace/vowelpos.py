from vowelspace.cardinals import make_backness_fn, make_height_fn
from vowelspace.diagram import Vowel
from argparse import ArgumentParser
from vowelspace.fmt import show_float

def main():
    parser = ArgumentParser(description='calculates vowel backness')
    parser.add_argument('-f1',
            '--formant1',
            required=True,
            metavar='X',
            type=float,
            dest='f1',
            help='formant 1 frequency (Hz)')
    parser.add_argument('-f2',
            '--formant2',
            required=True,
            metavar='Y',
            type=float,
            dest='f2',
            help='formant 2 frequency (Hz)')
    parser.add_argument('-r',
            '--roundedness',
            required=True,
            metavar='Z',
            type=float,
            dest='round',
            help='level of roundedness [0,1]')

    args = parser.parse_args()

    backness_fn = make_backness_fn()
    backness = backness_fn(args.f1, args.f2, args.round)
    height_fn = make_height_fn()
    height = height_fn(args.f1, args.f2, args.round)
    x, y = Vowel(backness=backness, height=height).pos()
    print(show_float(x))
    print(show_float(y))
