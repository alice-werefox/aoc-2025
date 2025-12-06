/*  Filename: main.cpp
 *  Author: Alice Winters
 *  Created: 05/12/2025
 */

#include <fstream>
#include <iostream>
#include <vector>

#include "produce_database.h"
#include "read_input.h"

const std::string INPUT_FILEPATH = "input/test_ingredients.txt";

int main()
{
    produce_database produce_db = read_input_from_file(INPUT_FILEPATH);
    for (int i = 0; i < produce_db.get_fresh_ranges_size(); i++)
    {
        std::cout << produce_db.get_fresh_range_from_index(i) << std::endl;
    }

    return 0;
}
