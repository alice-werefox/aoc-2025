#ifndef READ_INPUT_H

#define READ_INPUT_H

#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include "produce_database.h"

produce_database read_input_from_file(std::string filepath);

#endif