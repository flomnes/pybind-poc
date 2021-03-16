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

## TODO
Programs hangs, does not exit.
