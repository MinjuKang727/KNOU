#include <stdio.h>

int main()
{
	char ch1;
	ch1 = 'A';  // 코드값(10진수):65 >> (16진수):41
	printf("ch1 = '%c'\n", ch1);
	printf("'%c'의 ASCII 코드 = %d\n", ch1, ch1);
	
	char ch2 = 0x42;  // (16진수) 42 >> (10진수) 66 >> 문자 'B'
	printf("ASCII 코드 %d의 문자 = '%c'\n", ch2, ch2);
}