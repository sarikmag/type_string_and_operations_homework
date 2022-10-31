def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    a=f'({x}+{y})*2={(x+y)*2}'
    return a
print(main(4, 6))