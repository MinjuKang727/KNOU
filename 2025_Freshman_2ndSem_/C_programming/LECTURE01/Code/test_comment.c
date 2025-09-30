/* 두 수를 입력 받아
	덧셈 후 출력함   */
#include <stdio.h>
int main()
{
	int x, y, sum;  //변수 선언문
	/* 변수 x, y를 입력 받음 */
	printf("x = ");
	scanf("%d", &x);
	printf("y = ");
	scanf("%d", &y);
	
	// 두 수를 더해 변수 sum에 저장
	sum = x + y;

	// 결과를 화면에 출력
	printf("sum = %d", sum);
}