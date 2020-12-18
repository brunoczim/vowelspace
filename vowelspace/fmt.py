def show_float(num: float) -> str:
    '''
    Formats a float number up to 6 decimal places, cutting trailing zeroes
    '''
    return '{0:.6f}'.format(num).rstrip('0').rstrip('.')
