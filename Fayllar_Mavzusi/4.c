#include <stdio.h>

int Tubga_tekshir(int num) {
    if (num <= 1) return 0; 
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return 0; 
    }
    return 1; 
}
int main() {
    int N = 10; 
    FILE *file = fopen("tublar.txt", "w"); 

    if (file == NULL) {
        printf("Fayl ochishda xatolik!\n");
        return 1;
    }
    for (int i = 2; i < N; i++) { 
        if (Tubga_tekshir(i)) {
            fprintf(file, "%d ", i); 
        }
    }
    fclose(file); 
    printf("Tub sonlar 'tublar.txt' fayliga yozildi.\n");
    
    return 0;
}
