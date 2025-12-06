#ifndef PRODUCE_DATABASE_H

#define PRODUCE_DATABASE_H

#include <vector>
#include <string>

class produce_database
{
private:
    std::vector<std::string> fresh_ingredient_id_ranges;
    std::vector<std::string> available_ingredient_ids;

public:
    int get_fresh_ranges_size();
    std::string get_fresh_range_from_index(int index);
    void add_fresh_range(std::string range);
};

#endif