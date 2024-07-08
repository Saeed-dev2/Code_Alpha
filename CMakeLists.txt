project(test)

cmake_minimum_required(VERSION 3.1.0)

include_directories(${CMAKE_SOURCE_DIR}/mainFiles/include)

add_executable(test main.c ${CMAKE_SOURCE_DIR}/mainFiles/src/mainFiles.c)