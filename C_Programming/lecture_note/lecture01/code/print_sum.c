/* 도입부 */
# include <stdio.h>
int add(int x, int y);

/* main 함수 */
int main()
{
	int i = 10, j = 20, sum;
	sum = add(i, j);
	printf("%d+%d=%d", i, j, sum);
}

/* 프로그램에 필요한 함수 선언 */
int add(int x, int y)
{
	return x + y;
}

