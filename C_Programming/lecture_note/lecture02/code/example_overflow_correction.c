#include <stdio.h>
#include <limits.h>

int main()
{
	int num1, num2;  // 값을 수용할 수 있는 자료형
	
	num1 = 32767 + 1;
	num2 = -32768 - 1;
	
	printf("int 자료형 범위: %d ~ %d\n", INT_MIN, INT_MAX);
	printf("num1 = %d\n", num1);
	printf("num2 = %d\n", num2);
}