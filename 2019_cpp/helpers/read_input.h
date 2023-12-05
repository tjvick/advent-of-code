#include <iostream>
#include <fstream>
#include <string>
#include <list>

#ifndef INC_2019_CPP_READ_INPUT_H
#define INC_2019_CPP_READ_INPUT_H

std::list<std::string> read_file_as_list_of_strings(std::string filepath) {
  std::ifstream input_file (filepath, std::ifstream::in);

  std::list<std::string> file_contents;
  char line[2048];
  if (input_file.is_open()) {
    while (input_file.good()) {
      input_file.getline(line, 2048);
      std::string line_contents = std::string(line);
      file_contents.push_back(line_contents);
    }
  }

  return file_contents;
}

#endif // INC_2019_CPP_READ_INPUT_H
