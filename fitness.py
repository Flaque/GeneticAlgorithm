def hamming_distance(x, y):
    """ Computes the distance between two strings """
    assert len(x) == len(y)
    return sum(ch1 != ch2 for ch1, ch2 in zip(x, y))
