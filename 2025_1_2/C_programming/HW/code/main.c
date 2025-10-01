// [예제 3] 다음 세 개의 소스코드에서 중복되는 부분을 헤더파일로 만들어 수정하라.
#include <stdio.h>
#include "d.h"
#include "f.c"
#include "g.c"
#include "myName.h"

int main() {
    Hello;
    int a = 15, b = 10, c = 25;
    printf("%d, %d, %d\n", A, B, C);
    printf("%d\n", f(a, b, c) + g(a, b, c));
}