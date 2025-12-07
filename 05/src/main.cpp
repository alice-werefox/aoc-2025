/*  Filename: main.cpp
 *  Author: Alice Winters
 *  Created: 05/12/2025
 */

#include "produce_database.h"

const std::string INPUT_FILEPATH = "input/ingredients.txt";

int main()
{
    produce_database produce_db(INPUT_FILEPATH);
    // produce_db.debug_fresh_ranges();
    // produce_db.debug_available_ids();
    produce_db.union_ranges();
    // produce_db.debug_fresh_ranges();
    int64_t available_fresh_ingredients = produce_db.get_available_fresh_ids();
    std::cout << "Available fresh ingredients: " << available_fresh_ingredients << std::endl;
    int64_t fresh_ingedients = produce_db.get_fresh_ids();
    std::cout << "Total fresh ingredients: " << fresh_ingedients << std::endl;
    return 0;
}
