#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    FILE *fp;
    fp = fopen("values.dat", "w"); // Open for writing in text mode

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
	double x, y;
    
    for (x = -10; x <= 26; x += 0.1) {
        y = x*x - 16*x + 25;
        fprintf(fp, "%lf %lf\n", x, y); 
    }

    fclose(fp); // Close the file

    return 0;
}
