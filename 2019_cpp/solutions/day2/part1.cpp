#include <fstream>
#include <iostream>
#include <list>
#include <vector>

std::list<std::string> read_file_as_list_of_strings(std::string filepath) {
  std::ifstream input_file (filepath, std::ifstream::in);

  std::list<std::string> file_contents;
  char line[512];
  if (input_file.is_open()) {
    while (input_file.good()) {
      input_file.getline(line, 512);
      std::string line_contents = std::string(line);
      file_contents.push_back(line_contents);
    }
  }

  return file_contents;
}

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

void printVector(std::vector<int> vector_to_print) {
  std::cout << "[";
  for (auto str: vector_to_print) {
    std::cout << str << ", ";
  }
  std::cout << "]" << std::endl;
}

std::vector<int> list_to_vector(std::list<int> list_to_convert) {
  return std::vector<int> {list_to_convert.begin(), list_to_convert.end()};
}

std::list<int> csv_to_integer_list(std::string comma_separated_values) {
  std::list<int> int_list;
  std::string current = "";
  for (auto ch : comma_separated_values) {
    if (ch == ',') {
      int_list.push_back(stoi(current));
      current = "";
    } else {
      current.push_back(ch);
    }
  }
  int_list.push_back(stoi(current));
  return int_list;
}

int main() {
  auto fileContents = read_file_as_list_of_strings("./solutions/day2/input");
  std::cout << "# of rows in file: " << fileContents.size() << std::endl;

  auto firstLine = fileContents.front();
  std::cout << "First line in file: " << firstLine << std::endl;

  auto integerList = csv_to_integer_list(firstLine);
  auto intCodeMemory = list_to_vector(integerList);
  printVector(intCodeMemory);

  intCodeMemory[1] = 12;
  intCodeMemory[2] = 2;

  int instructionPointer = 0;
  while (true) {
    int opCode = intCodeMemory[instructionPointer];
    if (opCode == 99) {
      std::cout << "break!" << std::endl;
      break;
    }
    auto address1 = intCodeMemory[instructionPointer +1];
    auto address2 = intCodeMemory[instructionPointer +2];
    auto address3 = intCodeMemory[instructionPointer +3];
    std::cout << address1 << " " << address2 << " " << address3 << std::endl;
    auto operand1 = intCodeMemory[address1];
    auto operand2 = intCodeMemory[address2];
    if (opCode == 1) {
      auto sum = operand1 + operand2;
      intCodeMemory[address3] = sum;
    } else if (opCode == 2) {
      auto product = operand1 * operand2;
      intCodeMemory[address3] = product;
    }
    instructionPointer += 4;
    if (instructionPointer > intCodeMemory.size()) {
      break;
    }

    printVector(intCodeMemory);
  }

  printVector(intCodeMemory);
  std::cout << "Value in position 0: " << intCodeMemory[0] << std::endl;
}