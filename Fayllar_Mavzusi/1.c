#include <stdio.h>
#include <string.h>

int main() {
    char malumot[100];
    char fileName[] = "output.txt";
    printf("Familiya, ism, sharif va tugilgan sanangizni kiriting :\n");
    // masalan: Sattarov Akbar Baxtiyarovich 01.01.2001
    fgets(malumot, sizeof(malumot), stdin);
    FILE *file = fopen(fileName, "w");
    if (file == NULL) {
        printf("Faylni ochishda xatolik yuz berdi.\n");
        return 1;
    }
    char familya[50], ism[50], sharif[50], tugilgan_sana[15];
    sscanf(malumot, "%s %s %s %s", familya, ism, sharif, tugilgan_sana);
    fprintf(file, "%s\n", familya);
    fprintf(file, "%s\n", ism);
    fprintf(file, "%s\n", sharif);
    fprintf(file, "%s\n", tugilgan_sana);
    fclose(file);
    printf("Ma'lumotlar faylga yozildi.\n");

    return 0;
}
