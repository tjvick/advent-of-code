#include <iostream>
#include <string>
#include "read_input.h"

int calculateFuelRequirements(int mass) {
  auto fuel_for_mass = mass / 3 - 2;
  if (fuel_for_mass <= 0) {
    return 0;
  }

  return fuel_for_mass + calculateFuelRequirements(fuel_for_mass);
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
