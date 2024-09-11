#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main() {
    FILE *file;
    char ch;
    int soz = 0, gap = 0;
    int soni = 0;

    file = fopen("input.txt", "r");
    if (file == NULL) {
        printf("Fayl ochilmadi!\n");
        return 1;
    }
    while ((ch = fgetc(file)) != EOF) {
        if (isspace(ch) || ispunct(ch)) {
            if (soni) {
                soni = 0; 
                soz++;
            }
        } else {
            soni = 1; 
        }
        if (ch == '.' || ch == '!' || ch == '?') {
            gap++;
        }
    }
    if (soni) {
        soz++;
    }
    printf("%d ta so'z\n", soz);
    printf("%d ta gap\n", gap);
    fclose(file);
    
    return 0;
}
