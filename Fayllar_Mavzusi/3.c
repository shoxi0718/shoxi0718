#include <stdio.h>

int main() {
    int N;
        printf("N ni kiriting: ");
    scanf("%d", &N);
    
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Fayl ochishda xatolik yuz berdi.\n");
        return 1;
    }
    if (N % 2 == 0) { 
        for (int i = 1; i <= N; i++) {
            fprintf(file, "%d", i);
            for (int j = 1; j < i; j++) {
                fprintf(file, "+%d", i);
            }
            fprintf(file, "=%d\n", i * i);
        }
    } else { 
        for (int i = N; i >= 1; i--) {
            fprintf(file, "%d", i);
            for (int j = 1; j < i; j++) {
                fprintf(file, "+%d", i);
            }
            fprintf(file, "=%d\n", i * i);
        }
    }
    fclose(file);
    printf("Natijalar faylga yozildi.\n");
    
    return 0;
}
