def show_float(num: float) -> str:
    return '{0:.6f}'.format(num).rstrip('0').rstrip('.')
