#ifndef MERGE_SORT_H

#define MERGE_SORT_H

#include <iostream>
#include <vector>
#include <tuple>
#include <stdint.h>

void merge(std::vector<std::tuple<int64_t, int64_t>> &vec, int left, int mid, int right);
void mergeSort(std::vector<std::tuple<int64_t, int64_t>> &vec, int left, int right);

#endif