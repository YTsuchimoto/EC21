# New mutation operator with the deap library

The provided script solves the one max problem with float values (individual genes are real numbers initialized uniformly in the interval [0,1]), through
regular GA, with two point crossover and tournament selection of size 3.

The optimal solution to the problem is 100.0.

## Multiplicative Gaussian Noise

If a gene _g_ gets mutated with this operator, we have :

_g'_ = _g_ + (1 + _GN_)

Where _g'_ is the obtained mutation, and _GN_ a value sampled from a Normal distribution, bounded by the interval [-GN_POW, GN_POW], GN_POW<1.

## Results

The algorithm converges rappidly to a solution close to 100.0.

