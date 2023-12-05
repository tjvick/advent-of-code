#include "../../helpers/read_input.h"
#include <iostream>
#include <string>

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
