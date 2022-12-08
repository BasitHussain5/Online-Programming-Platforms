/*
This code take input from user and print on screen
*/

#include <stdio.h>

int main()
{
    char str[100];
    int i;
    //This code take input from user and print
    printf("Enter value:");
    scanf("%s%d",str,&i);
    printf("\nYou enterd:%s::::::%d", str,i);
    return 0;
}
