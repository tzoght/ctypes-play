//
// Created by Tony Zoght on 2016-07-13.
//
#include <stdio.h>
#include "../include/lib.h"


int multiply_by_two(int num) {
  return num*2;
}

void pass_array(char** props) {
  if (props == NULL) {
    printf("In pass_array(), props is NULL\n");
    return;
  }
  char** curr = props;
  printf("Printing list elements:\n");
  int i=0;
  while(*curr != NULL) {
    printf("%d-%s\n",i,*curr);
    curr = curr+1;
  }
}

/**
 * Assumes you have allocated
 */
int populate_string(char* buffer, int size) {
  if (size > 6) {
    strcpy(buffer,"Hello");
    return 1; // true
  } else {
    return 0 ; // false
  }
}
