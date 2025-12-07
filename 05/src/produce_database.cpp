#include "produce_database.h"
#include "read_input.h"
#include "merge_sort.h"

void produce_database::parse_input(std::vector<std::string> input_ranges, std::vector<std::string> input_ids)
{
    std::string temp_string;
    std::tuple<int64_t, int64_t> temp_tuple;
    for (int i = 0; i < (int)input_ranges.size(); i++)
    {
        temp_string = "";
        for (int j = 0; j < (int)input_ranges[i].size(); j++)
        {
            if (input_ranges[i][j] == '-')
            {
                std::get<0>(temp_tuple) = std::stoll(temp_string);
                temp_string = "";
                continue;
            }
            temp_string.push_back(input_ranges[i][j]);
        }
        std::get<1>(temp_tuple) = std::stoll(temp_string);
        this->fresh_ingredient_id_ranges.push_back(temp_tuple);
    }

    for (int i = 0; i < (int)input_ids.size(); i++)
    {
        this->available_ingredient_ids.push_back(std::stoll(input_ids[i]));
    }

    return;
}

produce_database::produce_database(std::string filename)
{
    std::tuple<std::vector<std::string>, std::vector<std::string>> input = read_input_from_file(filename);
    this->parse_input(std::get<0>(input), std::get<1>(input));
}

int produce_database::get_fresh_ranges_size()
{
    return this->fresh_ingredient_id_ranges.size();
}

std::tuple<int64_t, int64_t> produce_database::get_fresh_range_from_index(int index)
{
    return this->fresh_ingredient_id_ranges[index];
}

int produce_database::get_available_ids_size()
{
    return this->available_ingredient_ids.size();
}

int64_t produce_database::get_available_id_from_index(int index)
{
    return this->available_ingredient_ids[index];
}

void produce_database::debug_fresh_ranges()
{
    for (int i = 0; i < (int)this->get_fresh_ranges_size(); i++)
    {
        std::cout << std::get<0>(this->get_fresh_range_from_index(i));
        std::cout << "-";
        std::cout << std::get<1>(this->get_fresh_range_from_index(i));
        std::cout << std::endl;
    }
}

void produce_database::debug_available_ids()
{
    for (int i = 0; i < (int)this->get_available_ids_size(); i++)
    {
        std::cout << this->get_available_id_from_index(i) << std::endl;
    }
}

void produce_database::union_ranges()
{
    mergeSort(this->fresh_ingredient_id_ranges, 0, (int)this->fresh_ingredient_id_ranges.size() - 1);

    std::tuple<int64_t, int64_t> temp_tuple = this->fresh_ingredient_id_ranges[0];
    std::vector<std::tuple<int64_t, int64_t>> unioned_ranges;
    for (int i = 1; i < (int)this->get_fresh_ranges_size(); i++)
    {
        if (std::get<1>(temp_tuple) > std::get<1>(this->fresh_ingredient_id_ranges[i]))
        {
            continue;
        }
        if (std::get<1>(temp_tuple) < std::get<0>(this->fresh_ingredient_id_ranges[i]))
        {
            std::cout << std::get<0>(temp_tuple) << "-" << std::get<1>(temp_tuple) << std::endl;
            unioned_ranges.push_back(temp_tuple);
            temp_tuple = this->fresh_ingredient_id_ranges[i];
            continue;
        }
        std::get<1>(temp_tuple) = std::get<1>(this->fresh_ingredient_id_ranges[i]);
    }
    unioned_ranges.push_back(temp_tuple);

    this->fresh_ingredient_id_ranges = unioned_ranges;

    return;
}

int64_t produce_database::get_available_fresh_ids()
{
    int count = 0;

    for (int i = 0; i < (int)this->available_ingredient_ids.size(); i++)
    {
        for (int j = 0; j < (int)this->fresh_ingredient_id_ranges.size(); j++)
        {
            if (this->available_ingredient_ids[i] >= std::get<0>(this->fresh_ingredient_id_ranges[j]) && this->available_ingredient_ids[i] <= std::get<1>(this->fresh_ingredient_id_ranges[j]))
            {
                ++count;
                break;
            }
        }
    }

    return count;
}

int64_t produce_database::get_fresh_ids()
{
    int64_t sum = 0;

    for (int i = 0; i < (int)this->fresh_ingredient_id_ranges.size(); i++)
    {
        sum += std::get<1>(this->fresh_ingredient_id_ranges[i]) - std::get<0>(this->fresh_ingredient_id_ranges[i]) + 1;
    }

    return sum;
}