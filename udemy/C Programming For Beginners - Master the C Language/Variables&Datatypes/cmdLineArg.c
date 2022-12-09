#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int numberOfArg = argc;
    char *arg1 = argv[0];
    char *arg2 = argv[1];
    char *arg3 = argv[2];
    char *arg4 = argv[3];
    printf("Number of Arguments: %d\n", numberOfArg);
    printf("Argument1 is %s\n", arg1);
    printf("Argument2 is %s\n", arg2);
    printf("Argument3 is %s\n", arg3);
    printf("Argument4 is %s\n", arg4);


   return 0;
}
