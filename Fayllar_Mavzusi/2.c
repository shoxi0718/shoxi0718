#include <stdio.h>

int main() {
    int son[5];
    int sum = 0;
    char fileName[] = "new.txt";
    printf("5 ta son kiriting :\n");
    for (int i = 0; i < 5; i++) {
        scanf("%d", &son[i]);
        sum += son[i];
    }
        FILE *file = fopen(fileName, "w");
    if (file == NULL) {
        printf("Faylni ochishda xatolik yuz berdi.\n");
        return 1;
    }
    for (int i = 0; i < 5; i++) {
        fprintf(file, "%d", son[i]);
        if (i < 4) {
            fprintf(file, "+");
        }
    }
    fprintf(file, "=%d\n", sum);
    fclose(file);
    printf("Ma'lumotlar faylga yozildi.\n");

    return 0;
}
