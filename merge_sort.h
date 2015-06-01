#pragma once
#include "config.h"
#include <vector>

void merge(std::vector<int>& L, int begin, int mid, int end,std::vector<int>& tmp)
{
	int i = begin;
	int j = mid + 1;
	int k = 0;
	while(i <= mid && j <= end)
	{
		if(L[i] > L[j])
			tmp[k++] = L[j++];
		else
			tmp[k++] = L[i++];
	}
	while(i <= mid)
		tmp[k++] = L[i++];
	while(j <= end)
		tmp[k++] = L[j++];
	for(int m = 0; m < k; ++m)
		L[begin + m] = tmp[m];
}

void merge_sort(std::vector<int>& L, int begin, int end, std::vector<int>& tmp)
{
	if(begin < end)
	{
		int mid = begin + (end - begin) / 2;
		merge_sort(L, begin, mid, tmp);
		merge_sort(L, mid + 1, end, tmp);
		merge(L, begin, mid, end, tmp);
	}
}