#include <iostream>
#include <list>
#include <vector>

#ifndef INC_2019_CPP_PRINT_SEQUENCES_H
#define INC_2019_CPP_PRINT_SEQUENCES_H

void printList(std::list<std::string> list_to_print) {
  std::cout << "[";
  for (auto str: list_to_print) {
    std::cout << str << ", ";
  }
  std::cout << "]" << std::endl;
}

void printList(std::list<int> list_to_print) {
  std::cout << "[";
  for (auto str: list_to_print) {
    std::cout << str << ", ";
  }
  std::cout << "]" << std::endl;
}

void printVector(std::vector<std::string> vector_to_print) {
  std::cout << "[";
  for (auto str: vector_to_print) {
    std::cout << str << ", ";
  }
  std::cout << "]" << std::endl;
}

void printVector(std::vector<int> vector_to_print) {
  std::cout << "[";
  for (auto str: vector_to_print) {
    std::cout << str << ", ";
  }
  std::cout << "]" << std::endl;
}

#endif // INC_2019_CPP_PRINT_SEQUENCES_H
