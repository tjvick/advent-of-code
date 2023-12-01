cmake_minimum_required(VERSION 3.24)
project(2019_cpp)

set(CMAKE_CXX_STANDARD 14)

add_executable(2019_1_part_1
        solutions/day1/part1.cpp)
add_executable(2019_1_part_2
        solutions/day1/part2.cpp)
add_executable(2019_2_part_1
        solutions/day2/part1.cpp)
add_executable(2019_2_part_2
        solutions/day2/part2.cpp)
add_executable(sandbox_version_check
        solutions/sandbox/cpp_version_check.cpp)