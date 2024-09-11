#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void Fayl_saqla(const char *filename, int arr[], int size, int ascending) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Fayl ochishda xato");
        return;
    }
        for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if ((ascending && arr[i] > arr[j]) || (!ascending && arr[i] < arr[j])) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    for (int i = 0; i < size; i++) {
        fprintf(file, "%d ", arr[i]);
    }
    fclose(file);
}
int main() {
    srand(time(0)); 
    int A[10];
    for (int i = 0; i < 10; i++) {
        A[i] = rand() % (50 - (-50) + 1) + (-50);
    }
   int evens[10], even_count = 0;
    int odds[10], odd_count = 0;
        int positives[10], positive_count = 0;
             int negatives[10], negative_count = 0;
   for (int i = 0; i < 10; i++) {
       if (A[i] % 2 == 0) {
           evens[even_count++] = A[i];
       } else {                       
           odds[odd_count++] = A[i];
       }
       if (A[i] > 0) {               
           positives[positive_count++] = A[i];
       } else if (A[i] < 0) {          
           negatives[negative_count++] = A[i];
       }
   }
   Fayl_saqla("Juft.txt", evens, even_count, 1);         
   Fayl_saqla("Toq.txt", odds, odd_count, 0);           
   Fayl_saqla("Musbat.txt", positives, positive_count, 0);     
   Fayl_saqla("Manfiy.txt", negatives, negative_count, 1);      

   return 0;
}
