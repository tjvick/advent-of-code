cmake_minimum_required(VERSION 3.24)
project(2019_cpp)

set(CMAKE_CXX_STANDARD 14)


add_executable(2019_1_part_1 solutions/day1/part1.cpp)
target_include_directories(2019_1_part_1 PRIVATE helpers)

add_executable(2019_1_part_2 solutions/day1/part2.cpp)
target_include_directories(2019_1_part_2 PRIVATE helpers)

add_executable(2019_2_part_1 solutions/day2/part1.cpp)
target_include_directories(2019_2_part_1 PRIVATE helpers)

add_executable(2019_2_part_2 solutions/day2/part2.cpp)
target_include_directories(2019_2_part_2 PRIVATE helpers)

add_executable(2019_day3 solutions/day3/day3.cpp)
target_include_directories(2019_day3 PRIVATE helpers)