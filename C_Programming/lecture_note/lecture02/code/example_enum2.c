#include <stdio.h>

int main()
{
	enum day {SUN, MON, TUE, WED, THU, FRI, SAT};
	enum fruit {APPLE, PEAR, MANGO=4, GRAPE};
	
	printf("[열거형 변수 day의 값 출력하기]\n");
	printf("SUN의 값 = %d\n", SUN);
	printf("MON의 값 = %d\n", MON);
	printf("TUE의 값 = %d\n", TUE);
	printf("WED의 값 = %d\n", WED);
	printf("THU의 값 = %d\n", THU);
	printf("FRI의 값 = %d\n", FRI);
	printf("SAT의 값 = %d\n", SAT);
	
	printf("\n[열거형 변수 fruit의 값 출력하기]\n");
	printf("APPLE의 값 = %d\n", APPLE);
	printf("PEAR의 값 = %d\n", PEAR);
	printf("MANGO의 값 = %d\n", MANGO);
	printf("GRAPE의 값 = %d\n", GRAPE);
}