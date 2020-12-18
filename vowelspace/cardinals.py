from typing import NamedTuple, Tuple, List
import numpy as np
from scipy.interpolate import Rbf 

class Cardinal(NamedTuple):
    '''
    Data of a cardinal vowel.
    '''
    f1: float
    f2: float
    roundedness: float
    height: float
    backness: float

def to_f1_array(cards: List[Cardinal]) -> np.ndarray:
    '''
    Converts a list of cardinals to an array of F1 frequencies.
    '''
    f1s = list(map(lambda card: card.f1, cards))
    return np.array(f1s)

def to_f2_array(cards: List[Cardinal]) -> np.ndarray:
    '''
    Converts a list of cardinals to an array of F2 frequencies.
    '''
    f2s = list(map(lambda card: card.f2, cards))
    return np.array(f2s)

def to_roundedness_array(cards: List[Cardinal]) -> np.ndarray:
    '''
    Converts a list of cardinals to an array of roundness levels.
    '''
    roundednesss = list(map(lambda card: card.roundedness, cards))
    return np.array(roundednesss)

def to_height_array(cards: List[Cardinal]) -> np.ndarray:
    '''
    Converts a list of cardinals to an array of heights.
    '''
    heights = list(map(lambda card: card.height, cards))
    return np.array(heights)

def to_backness_array(cards: List[Cardinal]) -> np.ndarray:
    '''
    Converts a list of cardinals to an array of backnesses.
    '''
    backnesss = list(map(lambda card: card.backness, cards))
    return np.array(backnesss)

def to_height_arrays(cards: List[Cardinal]) -> List[np.ndarray]:
    '''
    Converts a list of cardinals to a list of arrays, where each array is an
    array of a cardinal vowels' field, such that the "output" array is the
    array of heights.
    '''
    return [
            to_f1_array(cards),
            to_f2_array(cards),
            to_roundedness_array(cards),
            to_height_array(cards)
            ]

def to_backness_arrays(cards: List[Cardinal]) -> List[np.ndarray]:
    '''
    Converts a list of cardinals to a list of arrays, where each array is an
    array of a cardinal vowels' field, such that the "output" array is the
    array of heights.
    '''
    return [
            to_f1_array(cards),
            to_f2_array(cards),
            to_roundedness_array(cards),
            to_backness_array(cards)
            ]

def make_rbf(arrays: List[np.ndarray]) -> Rbf:
    '''
    Converts a list of arrays of the same size into a function that
    interpolates the points formed by corresponding elements of the array.
    '''
    return Rbf(*arrays, function='cubic')

def make_height_fn() -> Rbf:
    '''
    Interpolates a height function from cardinals.
    '''
    return make_rbf(to_height_arrays(cardinals))

def make_backness_fn() -> Rbf:
    '''
    Interpolates a backness function from cardinals.
    '''
    return make_rbf(to_backness_arrays(cardinals))

# Data for interpolation. Not only helps interpolation but also delimites
# minimum and maximum.
cardinals = [
        Cardinal(f1=240, f2=2400, roundedness=0, height=3, backness=0),
        Cardinal(f1=235, f2=2100, roundedness=1, height=3, backness=0),
        Cardinal(f1=390, f2=2300, roundedness=0, height=2, backness=0),
        Cardinal(f1=370, f2=1900, roundedness=1, height=2, backness=0),
        Cardinal(f1=610, f2=1900, roundedness=0, height=1, backness=0),
        Cardinal(f1=585, f2=1710, roundedness=1, height=1, backness=0),
        Cardinal(f1=850, f2=1610, roundedness=0, height=0, backness=0),
        Cardinal(f1=820, f2=1530, roundedness=1, height=0, backness=0),
        Cardinal(f1=750, f2=940, roundedness=0, height=0, backness=2),
        Cardinal(f1=700, f2=760, roundedness=1, height=0, backness=2),
        Cardinal(f1=600, f2=1170, roundedness=0, height=1, backness=2),
        Cardinal(f1=500, f2=700, roundedness=1, height=1, backness=2),
        Cardinal(f1=460, f2=1310, roundedness=0, height=2, backness=2),
        Cardinal(f1=360, f2=640, roundedness=1, height=2, backness=2),
        Cardinal(f1=300, f2=1390, roundedness=0, height=3, backness=2),
        Cardinal(f1=250, f2=595, roundedness=1, height=3, backness=2),
        ]
