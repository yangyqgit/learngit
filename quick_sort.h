#pragma once
#include "config.h"
#include <vector>

int partition(std::vector<int>& L, int begin, int end)
{
	int i = begin;
	int temp = L[i];
	for (int j = begin + 1; j <= end; ++j)
	{
		if(L[j] <= temp)
			std::swap(L[++i], L[j]);
	}
	std::swap(L[i], L[begin]);
	return i;
}

void quick_sort(std::vector<int>& L, int begin, int end)
{
	if(begin < end)
	{
		int i = partition(L, begin, end);
		quick_sort(L, begin, i - 1);
		quick_sort(L, i + 1, end);
	}
}