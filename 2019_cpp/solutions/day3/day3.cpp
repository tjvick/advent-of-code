#include <iostream>
#include <string>
#include <sstream>
#include "../../helpers/read_input.h"
#include "../../helpers/print_sequences.h"

std::vector<std::string> split (const std::string &s, char delim) {
  std::vector<std::string> result;
  std::stringstream ss (s);
  std::string item;

  while (getline(ss, item, delim)) {
    result.push_back(item);
  }

  return result;
}


int part1() {
  auto input_strings = read_file_as_list_of_strings("./solutions/day3/test");
  auto iter = input_strings.begin();
  std::string wire_path_1 = *iter++;
  std::string wire_path_2 = *iter;

  printVector(split(wire_path_1, ','));
  printVector(split(wire_path_2, ','));
  std::cout << wire_path_2 << std::endl;
  return 0;
}

int part2() {
  return 2;
}

int main() {
  int answer = part1();
//  int answer = part2();
  std::cout << answer << std::endl;
}