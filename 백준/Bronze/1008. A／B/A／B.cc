#include <stdio.h>

int main(void) {
    double a = 0;
    double b = 0;
    scanf("%lf %lf", &a, &b);
    printf("%.13lf", a / b);
    return 0;
}