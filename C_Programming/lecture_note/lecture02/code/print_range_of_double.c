#include <stdio.h>
#include <float.h>

int main()
{
	double minDouble = DBL_MIN;
	double maxDouble = DBL_MAX;
	printf("double 자료형의 범위: %e ~ %e\n", minDouble, maxDouble);
}