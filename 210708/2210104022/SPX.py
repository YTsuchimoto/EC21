import numpy as np

try:
    from collections.abc import Sequence
except ImportError:
    from collections import Sequence

from itertools import repeat


def cxSimplexCrossover(inds):
    P = np.array(inds)
    G = np.sum(P, axis=0)
    eps = np.sqrt(len(P) + 1)
    x = G + eps * (P - G)
    r = np.array([0] + [np.random.rand() ** (1.0 / (k + 1)) for k in range(len(P) - 1)])
    C = np.zeros_like(P)
    # itertoolsとかにscan系の関数があれば...
    for k in range(1, len(P)):
        C[k] = r[k] * (x[k - 1] - x[k] + C[k - 1])
    return (x[-1] + C[-1]).tolist()


def cxSimplexCrossoverBounded(inds, low, up):
    size = min(map(len, inds))
    if not isinstance(low, Sequence):
        low = list(repeat(low, size))
    elif len(low) < size:
        raise IndexError("low must be at least the size of the shorter individual: %d < %d" % (len(low), size))
    if not isinstance(up, Sequence):
        up = list(repeat(up, size))
    elif len(up) < size:
        raise IndexError("up must be at least the size of the shorter individual: %d < %d" % (len(up), size))

    c = cxSimplexCrossover(inds)
    c = np.minimum(np.maximum(c, low), up)
    return c.tolist()
