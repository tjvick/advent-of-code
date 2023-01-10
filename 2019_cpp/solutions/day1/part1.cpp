#include <iostream>
#include <fstream>
#include <string>
#include <list>

std::list<std::string> read_file_as_list_of_strings(std::string filepath) {
  std::ifstream input_file (filepath, std::ifstream::in);

  std::list<std::string> file_contents;
  char line[256];
  if (input_file.is_open()) {
    while (input_file.good()) {
      input_file.getline(line, 256);
      std::string line_contents = std::string(line);
      file_contents.push_back(line_contents);
    }
  }

  return file_contents;
}

int calculateFuelRequirements(int mass) {
  return mass / 3 - 2;
}

int main() {
  auto file_contents = read_file_as_list_of_strings("./solutions/day1/input");

  int total_fuel_requirements = 0;
  for (auto line: file_contents) {
    if (!line.empty()) {
      auto mass = std::stoi(line);
      auto fuel_requirements = calculateFuelRequirements(mass);
      total_fuel_requirements += fuel_requirements;
    }
  }

  std::cout << "Total Fuel Requirements: " << total_fuel_requirements << std::endl;
}
