#include <stdio.h>
#include <limits.h>

int main()
{
	short int num1, num2;
	
	num1 = 32767 + 1;
	num2 = -32768 - 1;
	
	printf("short int 자료형 범위: %d ~ %d\n", SHRT_MIN, SHRT_MAX);
	printf("num1 = %d\n", num1);
	printf("num2 = %d\n", num2);
}