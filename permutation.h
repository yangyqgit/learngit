#pragma once
#include "config.h"

void permutation(char* str, char* begin)
{
	if(*begin == '\0')
	{
		printf("%s\n", str);
	}
	else
	{
		for (char* pch = begin; *pch != '\0'; ++pch)
		{
			std::swap(*begin, *pch);
			permutation(str, begin + 1);
			std::swap(*begin, *pch);
		}
	}
}