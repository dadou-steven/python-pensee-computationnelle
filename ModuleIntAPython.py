def subtract_lists(l1, l2):
    assert len(l1) == len(l2)
    out = []
    for ix in range(len(l1)):
        out.append(l1[ix] - l2[ix])
    return out
