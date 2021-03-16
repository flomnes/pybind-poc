## Summary
This is a POC to test mpi4py and pybind11. The goal is to send a pybind11 object to another thread and receive it. To do that, we need to handle serialization/deserialization.


## Limitations
Serialization/deserialization is handled with Pickle, through a `py::tuple` representation of objects containing basic types only (strings, ints, float, etc.).

Handling more complex data types (vectors, etc.) may be challenging.

## Dependencies
First, we need to install dependencies.

### pybind11
```bash
git submodule init
git submodule update
```

### mpi4py
```bash
python3 -m pip3 install -r requirements.txt
```

## Build
Configure build
```
cmake .
```

Build
```bash
cmake --build .
```

## Execution
```bash
mpirun python3 test.py
```

## Sources
[Pickling support](https://pybind11.readthedocs.io/en/stable/advanced/classes.html#pickling-support)

[mpi4py tutorial](https://mpi4py.readthedocs.io/en/stable/tutorial.html)
