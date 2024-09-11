#include <stdio.h>
#include <string.h>

int main() {
    FILE *file;
    char gap[1000];
    char soz[100];
    file = fopen("text.txt", "r");
    if (file == NULL) {
        printf("Faylni ochishda xatolik yuz berdi.\n");
        return 1;
    }
    while (fgets(gap, sizeof(gap), file)) {
        char *token = strtok(gap, " \t\n");
        while (token != NULL) {
            if (strlen(token) < 5) {
                printf("5tadan kam bo'lgan so'z: %s\n", token);
            }
            token = strtok(NULL, " \t\n");
        }
    }
    fclose(file);
    return 0;
}
