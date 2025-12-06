#include "read_input.h"
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include "produce_database.h"

using namespace std;

produce_database read_input_from_file(string filepath)
{
    produce_database produce_db;
    ifstream input_file(filepath);
    string input_buffer = " ";
    while (input_buffer != "")
    {
        getline(input_file, input_buffer);
        produce_db.add_fresh_range(input_buffer);
    }
    input_file.close();
    return produce_db;
}