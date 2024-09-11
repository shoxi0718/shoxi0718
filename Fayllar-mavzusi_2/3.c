#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    FILE *file;
    char line[100];
    char gap[100];
    char uzun[100];
    int katta, soz_uzun;

    file = fopen("text.txt", "r");
    if (file == NULL) {
        printf("Faylni ochishda xatolik yuz berdi.\n");
        return 1;
    }
    while (fgets(line, sizeof(line), file)) {
        katta = 0;
        uzun[0] = '\0'; 
        char *token = strtok(line, " \t\n");
        while (token != NULL) {
            soz_uzun = strlen(token);
            if (soz_uzun > katta) {
                katta = soz_uzun;
                strncpy(uzun, token, sizeof(uzun));
                uzun[sizeof(uzun) - 1] = '\0'; 
            token = strtok(NULL, " \t\n");
        }
        if (katta > 0) {
            printf("Eng uzun so'z: %s\n", uzun);
        }
    }
    fclose(file);
    return 0;
}
