#include <stdio.h>

int main() {
    FILE *file;
    char ch;
    int yig = 0;
    file = fopen("text.txt", "r");
    if (file == NULL) {
        printf("Faylni ochishda xatolik yuz berdi.\n");
        return 1;
    }
    while ((ch = fgetc(file)) != EOF) {
        if (ch == '\n') {
            yig++;
        }
    }
    if (yig > 0 || ftell(file) != 0) {
        yig++;
    }
    printf("Qatorlar soni: %d\n", yig);
    fclose(file);
    
    return 0;
}
