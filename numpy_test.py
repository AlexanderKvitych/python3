import numpy as np

def function_numpy():
    x = np.arange(15, dtype=np.int64).reshape(3, 5)
    x[1:, ::2] = -99
    x_1 = x.max(axis=1)
    rng = np.random.default_rng()
    samples = rng.normal(size=2500)
    print(f'array: {x}, \narray_1: {x_1}\nGenerate normally distributed random numbers: {samples}')
function_numpy()