from typing import NamedTuple, Tuple, List
from vowelspace.cardinals import max_height, max_backness

top = 50
bottom = 650
left0 = 100
left1 = 500
right = 900

class Vowel(NamedTuple):
    '''
    A preceived vowel.
    '''
    height: float
    backness: float

    def pos(self) -> Tuple[float, float]:
        '''
        Converts this vowel into a position on the trapezoid image.
        '''
        
        trapezoid_height = bottom - top
        height_correct = trapezoid_height / max_height
        y_coord = top + height_correct * (max_height - self.height)

        left_diff = left1 - left0
        left = left0 + (y_coord - top) / trapezoid_height * left_diff
        trapezoid_width = right - left
        width_correct = trapezoid_width / max_backness
        x_coord = left + width_correct * self.backness

        return x_coord, y_coord
