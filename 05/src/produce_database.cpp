#include "produce_database.h"
#include <vector>
#include <string>

int produce_database::get_fresh_ranges_size()
{
    return this->fresh_ingredient_id_ranges.size();
}

std::string produce_database::get_fresh_range_from_index(int index)
{
    return this->fresh_ingredient_id_ranges[index];
}

void produce_database::add_fresh_range(std::string range)
{
    this->fresh_ingredient_id_ranges.push_back(range);
    return;
}