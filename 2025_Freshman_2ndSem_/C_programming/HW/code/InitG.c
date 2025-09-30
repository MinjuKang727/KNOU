// [예제 5] 다음 두 코드를 각각 실행하여 결과를 구하고, 결과의 차이가 나는 이유를 설명하라.
#include <stdio.h>
#include "myName.h"

int x = 0;

int f() {
    x = x + 1;
    return x;
}

int main() {
    Hello;
    printf("%d\n", f());
    printf("%d\n", f());
    printf("%d\n", f());
}