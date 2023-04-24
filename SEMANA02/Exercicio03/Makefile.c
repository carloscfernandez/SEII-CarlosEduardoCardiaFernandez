APPS = ./apps
BIN = ./bin
INCLUDE = ./include
OBJ = ./obj
SRC = ./src

all: libed myapps

  gcc 
  gcc
  
libed;
  gcc -c $(SRC)/float_vector.c -I $(INCLUDE) -o .(OBJ)/float_vector.o
  gcc -c $(SRC)/mytime.c -I $(INCLUDE) -o .(OBJ)/mytime.o

myapps;
  gcc -c $(APPS)/app.c $(OBJ)/.o -I $(INCLUDE) -o .(BIN)/app
  gcc -c $(APPS)/app_com_mytime.c $(OBJ)/.o -I $(INCLUDE) -o .(BIN)/app_com_mytime.o
    
run;
  ./bin/app
    
clean;
  rm ./bin/
  rm ./obj/
    
    
