//  [예제 1] int형의 값을 두 개 입력하여 이들의 합과 곱 구하고, 그 값을 출력하는 프로그램을 완성하라.
#include <stdio.h>
#include "myName.h"

int main() {
    Hello;
    int a, b;       // int형 변수 a와 b를 선언
    int sum, mul;  // int형 변수 sum과 mul을 선언
    scanf("%d %d", &a, &b);  // a와 b에 값을 입력
    sum = a + b;
    mul = a * b;
    printf("%d + %d = %d\n", a, b, sum);  // a + b = sum 출력
    printf("%d * %d = %d\n", a, b, mul);  // a * b = mul 출력
}