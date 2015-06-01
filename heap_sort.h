#pragma once
#include "config.h"
#include <vector>
#include <algorithm>

void max_heapify(std::vector<int>& L, int i, int heap_size)
{
	int left = 2 * i + 1;
	int right = left + 1;
	int temp = L[i];
#ifndef FACTORIAL
	while(left < heap_size)
	{
		if(right < heap_size && L[right] > L[left])
			left = right;
		if(L[left] <= temp)
			break;
		L[i] = L[left];
		i = left;
		left = 2 * i + 1;
		right = left + 1;
	}
	L[i] = temp;
#else
	int largest = i;
	if(left < heap_size && L[left] > temp)
		largest = left;
	if(right < heap_size && L[right] > L[largest])
		largest = right;
	if(largest == i)
		return;
	L[i] = L[largest];
	L[largest] = temp;
	max_heapify(L, largest, heap_size);
#endif
}

void build_max_heap(std::vector<int>& L)
{
	int size = L.size();
	for (int i = size / 2 - 1; i >= 0; --i)
		max_heapify(L, i, size);
}

void heap_sort(std::vector<int>& L)
{
	int size = L.size();
	if(size != 0)
	{
		build_max_heap(L);
		for (int i = size - 1; i > 0; --i)
		{
			std::swap(L[0], L[i]);
			max_heapify(L, 0, i);
		}
	}
}