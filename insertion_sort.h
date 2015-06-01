#pragma once
#include "config.h"
#include <vector>

void insertion_sort(std::vector<int>& L)
{
	size_t size = L.size();
	for (int i = 1; i < size; ++i)
	{
		int j = i - 1;
		int temp = L[i];
		while(j >= 0 && L[j] > temp)
		{
			L[j + 1] = L[j];
			--j;
		}
		L[j + 1] = temp;
	}
}