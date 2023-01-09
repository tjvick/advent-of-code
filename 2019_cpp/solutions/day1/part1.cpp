#include <iostream>
#include <fstream>
#include <string>

int calculateFuelRequirements(int mass) {
  return mass / 3 - 2;
}

int main() {
  std::ifstream input_file ("./solutions/day1/input", std::ifstream::in);

  auto total_fuel_requirements = 0;
  char line[256];
  if ( input_file.is_open() ) {
    while (input_file.good()) {
      input_file.getline(line, 256);
      std::string mass_str = std::string(line);
      if (!mass_str.empty()) {
        auto mass = std::stoi(mass_str);
        auto fuel_requirements = calculateFuelRequirements(mass);
        total_fuel_requirements += fuel_requirements;
      }
    }
  }

  std::cout << "Total Fuel Requirements: " << total_fuel_requirements << std::endl;
}
