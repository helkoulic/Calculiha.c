#include <stdio.h>
#include <stdlib.h>

void Banner(){
    printf("Th3 C C4lcul4t0r!\n");
}

int main(){
    Banner();

    float Num1, Num2;
    float result;

    //(1) ? printf("thats true c:\n") : printf("bs\n");

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

// Handle float results

// IF the number is X.000000, print X
// Else, print the full number without zeroes

// Use type conversion to make the results that contain .0 integers
