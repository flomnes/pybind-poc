cmake_minimum_required(VERSION 3.0)
project(py-mpi LANGUAGES CXX)

add_subdirectory(pybind11)

pybind11_add_module(example example.cpp)

