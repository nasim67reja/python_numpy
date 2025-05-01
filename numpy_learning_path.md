
## Creating Arrays

NumPy provides several methods to create arrays efficiently. Here are some commonly used ones:

- `np.ones(shape)`: Creates an array filled with ones.  
   Example: `np.ones((3, 3))` → 3x3 matrix of ones.

- `np.zeros(shape)`: Creates an array filled with zeros.  
   Example: `np.zeros(5)` → 1D array of five zeros.

- `np.full(shape, fill_value)`: Creates an array filled with a specified value.  
   Example: `np.full((2, 2), 7)` → 2x2 matrix filled with 7.

- `np.arange(start, stop, step)`: Creates an array with a sequence of numbers.  
   Example: `np.arange(0, 10, 2)` → `[0, 2, 4, 6, 8]`.

- `np.linspace(start, stop, num)`: Creates an array with evenly spaced numbers over a specified range.  
   Example: `np.linspace(0, 1, 5)` → `[0. , 0.25, 0.5, 0.75, 1.]`.

- `np.random.rand(d0, d1, ...)`: Generates an array of random numbers between 0 and 1.  
   Example: `np.random.rand(3, 2)` → 3x2 matrix of random values.

- `np.random.randint(low, high, size)`: Generates an array of random integers within a range.  
   Example: `np.random.randint(1, 10, 5)` → 1D array of 5 random integers between 1 and 9.

- `np.eye(N)`: Creates an identity matrix of size `N`.  
   Example: `np.eye(3)` → 3x3 identity matrix.

- `np.empty(shape)`: Creates an uninitialized array of the specified shape.  
   Example: `np.empty((2, 3))` → 2x3 array with arbitrary values.

These methods are particularly useful for initializing data structures in algorithmic trading, such as price matrices, signal arrays, or synthetic datasets.
