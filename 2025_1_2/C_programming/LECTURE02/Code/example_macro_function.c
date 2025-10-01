#include <stdio.h>
#define C_AREA(x) (3.141592 * (x) * (x))

int main()
{
    double r = 10.0;
    printf("%lf\n", C_AREA(r));
}