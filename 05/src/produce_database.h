#ifndef PRODUCE_DATABASE_H

#define PRODUCE_DATABASE_H

#include <vector>
#include <string>
#include <iostream>
#include <stdint.h>

class produce_database
{
private:
    std::vector<std::tuple<int64_t, int64_t>> fresh_ingredient_id_ranges;
    std::vector<int64_t> available_ingredient_ids;
    void parse_input(std::vector<std::string> input_ranges, std::vector<std::string> input_ids);

public:
    produce_database(std::string filename);
    int get_fresh_ranges_size();
    std::tuple<int64_t, int64_t> get_fresh_range_from_index(int index);
    int get_available_ids_size();
    int64_t get_available_id_from_index(int index);
    void debug_fresh_ranges();
    void debug_available_ids();
    void union_ranges();
    int64_t get_available_fresh_ids();
    int64_t get_fresh_ids();
};

#endif