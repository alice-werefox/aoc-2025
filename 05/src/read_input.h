#ifndef READ_INPUT_H

#define READ_INPUT_H

#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include "produce_database.h"

std::tuple<std::vector<std::string>, std::vector<std::string>> read_input_from_file(std::string filepath);

#endif