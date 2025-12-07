#include "read_input.h"

using namespace std;

tuple<vector<string>, vector<string>> read_input_from_file(string filepath)
{
    vector<string> ranges;
    vector<string> ids;
    ifstream input_file(filepath);
    string input_buffer = " ";
    bool is_after_ranges = false;
    while (getline(input_file, input_buffer))
    {
        if (input_buffer == "")
        {
            is_after_ranges = true;
            continue;
        }
        if (is_after_ranges)
        {
            ids.push_back(input_buffer);
            continue;
        }
        ranges.push_back(input_buffer);
    }
    input_file.close();

    tuple<vector<string>, vector<string>> output(ranges, ids);
    return output;
}