#include <stdio.h>
#include <stdbool.h>

int main() {
    FILE *file;
    char ch;
    int yig = 0;
    bool a;
    file = fopen("text.txt", "r");
    if (file == NULL) {
        printf("Faylni ochishda xatolik yuz berdi.\n");
        return 1;
    }
    while (1) {
        a = false;
        while ((ch = fgetc(file)) != EOF && ch != '\n') {
            if (ch == 'p') {
                a = true;
            }
        }
        if (a) {
            yig++;
        }
        if (ch == EOF) {
            break;
        }
    }
    printf("Qatorlar soni  %d\n", yig);
    fclose(file);

    return 0;
}
