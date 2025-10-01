/*
[예제 6] 정수를 입력한 다음 그 값을 3으로 나눈 나머지가 0인 수, 1인 수, 2인 수의 합을 각각 구하려고 한다. 
정수 입력이 음수이면 반복을 중지하고 각각의 합을 출력한다. 
㈀과 ㈁을 완성하라. 
㈁은 if문을 이용하는 방법과 switch문을 이용하는 방법으로 각각 작성하라.
*/

#include <stdio.h>
#include "myName.h"

int main() {
    Hello;
    int sumR0, sumR1, sumR2, num;
    sumR0 = sumR1 = sumR2 = 0;
    printf("Input : ");
    scanf("%d", &num);
    while (num >= 0) {
        int remain = num % 3;

        if (remain == 0) {
            sumR0 += num;
        } else if (remain == 1) {
            sumR1 += num;
        } else {
            sumR2 += num;
        }
        
        printf("Input : ");
        scanf("%d", &num);
    }
    printf("나머지가 0인 수의 합 = %d\n", sumR0);
    printf("나머지가 1인 수의 합 = %d\n", sumR1);
    printf("나머지가 2인 수의 합 = %d\n", sumR2);
}