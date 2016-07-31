#include <stdio.h>
#include "../include/lib.h"
#include "cutest.h"

void test_hello_world(void)
{
    printf("Hello World");
    TEST_CHECK_((1 != 0 ),"1 should be equal to 0 !");
}

void test_multiply(void)
{
    int num = 2;
    int result = multiply_by_two(num);
    TEST_CHECK_((result == num*2),"ok");
}

void test_pass_array(void)
{
  char* list[3];
  list[0] = "item1";
  list[1] = "item2";
  list[2] = NULL;
  pass_array((char**)list);
  TEST_CHECK_((1==1),"ok");
}

TEST_LIST = {
        { "test_hello_world", test_hello_world },
        { "test_multiply", test_multiply},
        { "test_pass_array",test_pass_array},
        { 0 }
};
