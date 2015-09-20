/* fd-write-redirect.c */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <math.h>

int main( int argc, char * argv[])
{
  int fil = open(argv[1],'r');
  int num_by = atoi(argv[2]);
  struct stat buffer;
  lstat(argv[1],&buffer);
  float num_c = buffer.st_size/(float)num_by;
  float tnum_c = ceil(num_c);
  int num_proc = (int) tnum_c;
  printf("PARENT: File '%s' contains %d bytes\n",argv[1],(int)buffer.st_size);
  printf("PARENT: ... and will be processed via %d child processes\n",num_proc);
  pid_t pid;
  char* word_buffer;
  int check = 0;
  //pid = fork();
  while (check < num_proc) {
    pid = fork();
    if (pid > 0){
    	word_buffer = malloc(sizeof(char)*(num_by));
      read(fil,word_buffer,sizeof(char)*num_by);
      printf("CHILD %d CHUNK: %s",pid,word_buffer);
      fflush(stdout);
      check += 1;
    } 
    wait();
  }
}