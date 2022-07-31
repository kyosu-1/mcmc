#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double py_mc(int niter) {
    int n_in = 0;
    srand((unsigned)time(NULL));

    for (int i = 0; i < niter; i++) {
        double x = (double)rand() / RAND_MAX;
        double y = (double)rand() / RAND_MAX;
        if (x * x + y * y < 1e0) {
            n_in += 1;
        }
    }
    printf("%d\n", n_in);
    return ((double)n_in / niter)*4;
}

int main(void) {
    printf("%f\n", py_mc(1000));
    return 0;
}
