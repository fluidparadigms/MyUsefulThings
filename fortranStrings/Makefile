
OPT = -g3 -O0
#OPT = -O2
CPPFLAGS = $(OPT) -Wall --std=c++17 -isystem ~/fmt/install/include
#CPPFLAGS = $(OPT) -Wall -fPIC --std=c++14
#LDLIBS = -pthread -lrt
LDLIBS = -lstdc++fs -lifcore -ldl
TARGET_ARCH := -m64
FFLAGS := $(OPT)

all : run

run : test
	./test

test : main.o fort.o
	$(LINK.cc) $^ $(LOADLIBES) $(LDLIBS) -o $@

fort.o : fort.F90
	$(COMPILE.f) $(OUTPUT_OPTION) $<

clean :
	rm -rf test *.so *.o *.mod

.PHONY : clean all run

