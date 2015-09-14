/*
Joseph Monroe
Operating Systems Homework 1
RPI - 661220872
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char * argv[])
{
  if (argc != 3){
    printf("Must have 3 command line arguements\n");
    return 0;
  }
  int curlen = 20;
  int numwords = 0;
  int x = 0;
  FILE *maintext = fopen(argv[1],"r");
  printf("Allocated initial array of %d character pointers.\n",curlen);
  char** wordlis = (char**)calloc(curlen,sizeof(char*));
  
  char mystring[128] = {'\0'};
  while (x != EOF)
  {
      if (numwords > curlen){
        curlen *= 2;
        wordlis = (char**) realloc(wordlis,sizeof(char*)*curlen);
        printf("Reallocated array of %d character pointers.\n",curlen);
      }

      x = fscanf(maintext,"%s",mystring);
      wordlis[numwords] = (char*) malloc(sizeof(mystring));
      strcpy(wordlis[numwords], mystring);
      numwords++;
      


  }

  int i;

  for (i = 0; i < numwords;i++)
  {
    if (strncmp(argv[2],wordlis[i],strlen(argv[2])) == 0){
      printf("%s\n",wordlis[i]);
    }
    free(wordlis[i]);
  }
  fclose(maintext);
  free(wordlis);
  return 0;
}
