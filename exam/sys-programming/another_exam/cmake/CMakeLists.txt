#the minimum version required
cmake_minimum_required(VERSION 3.10)

#project's name
project(calculator)

# set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
# set(RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
# set(LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# include(${PROJECT_SOURCE_DIR})
include_directories(include)
file(GLOB SOURCES "src/*.cpp")

add_executable(myprogram ${SOURCES})