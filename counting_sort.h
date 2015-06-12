#pragma once
#include "config.h"
#include <vector>

void counting_sort(std::vector<int>& L, int begin, int end)
{
	if(begin == end || L.empty())
		return;
	int l,r;
	if(begin < end)
	{
		l = begin;
		r = end;
	}
	else
	{
		l = end;
		r = begin;
	}
	size_t size = r - l + 1;
	std::vector<int> index(size, 0);
	for (size_t i = 0; i < L.size(); ++i)
		++index[L[i]];
	int k = 0;
	for (size_t i = 0; i < size; ++i)
	{
		while(index[i] > 0)
		{
			L[k++] = i;
			--index[i];
		}
	}
}