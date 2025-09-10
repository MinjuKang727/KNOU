#include <stdio.h>

int main()
{
	enum day {SUN, MON, TUE, WED, THU, FRI, SAT};
	enum fruit {APPLE, PEAR, MANGO=4, GRAPE};
	
	printf("TUE의 값 = %d\n", TUE);
	printf("PEAR의 값 = %d\n", PEAR);
	printf("GRAPE의 값 = %d\n", GRAPE);
	printf(day);
	printf(fruit);
}