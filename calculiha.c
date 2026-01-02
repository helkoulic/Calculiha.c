#include <stdio.h>
#include <stdlib.h>


void Banner(){
    printf("Th3 C C4lcul4t0r!\n");
}

int main(){
    Banner();

    float Num1, Num2;
    float result;

    while (1){
        char Operation;
        printf("\n|===(First Number)===> ");
        scanf("%f", &Num1);

        printf("|===(+|-|*|/)===> ");
        scanf("%s", &Operation);

        printf("|===(Second Number)===> ");
        scanf("%f", &Num2);
        if (Operation == '+'){
            result = Num1 + Num2;
        }
        else if (Operation == '-'){
            result = Num1 - Num2;
        }
        else if (Operation == '*'){
            result = Num1 * Num2;
        }
        else if (Operation == '/'){
            // Handling the zero devision Error
            if (Num2 != 0){
                result = Num1 / Num2;
            }
            else{
                puts("You crazy or wat?");
            }
        }
        else{
            puts("Exiting..");
            exit(0);
        }
        printf("|===> %.6g %s %.6g = %.6g\n", Num1, &Operation, Num2, result);
        puts("____      ___     __    _");
    }

    return 0;
}
