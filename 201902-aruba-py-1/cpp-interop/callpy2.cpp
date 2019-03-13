#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <process.h>

int main(){
    
    FILE *f =  _popen("python greet.py vivek", "r");

  if (!f)
  {
    printf("error in code");
    return -1;
  }
  printf("python code finished executing...\n");
  
  char buffer[1024];
  while (! feof(f)){
      int ch=fgetc(f);
      printf("%c.",ch);

  }
  _pclose(f);
}