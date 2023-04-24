#ifndef MY_TIME_H
#define MY_TIME_H

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

// medindo tempo em C (Linux)
typedef struct timeval timer; //adicionando um novo nome para o tipo struct timeval

// função que marca o tempo atuaç
timer tic();

//marca o final do trecho do tempo;
timer tac();

float comptime(timer tic, timer tac);

#endif
