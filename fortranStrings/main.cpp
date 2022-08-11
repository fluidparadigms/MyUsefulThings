
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <optional>
#include <chrono>
#include <experimental/filesystem>
#include <cpuid.h>
#include <wordexp.h>

#define FMT_HEADER_ONLY
#include <fmt/format.h>
#include <fmt/ostream.h>

using namespace std;
namespace fs = std::experimental::filesystem;

extern "C" 
{
    void printversion_();

    const char* the_vers_str = "1.2.3.4";

    const char* getvers(size_t& slen)
    {
        slen = strlen(the_vers_str);
        return the_vers_str;
    }
}

int main(int argc, char** argv)
{

    printversion_();

    return 0;
}


