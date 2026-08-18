#include <cmath>
#include <cstddef>
#include <iomanip>
#include <iostream>
#include <sstream>

int main(int argc, char *argv[])
{
    const std::size_t hashcode = 0x21'DD'09'EC;
    std::size_t       copy     = hashcode;
    std::size_t       c;

    std::stringstream ss;

    for (int i = 0; i < 5; i++)
    {
        if (i < 4)
            c = 0x01'01'01'01;
        else
            c = copy;
        copy -= c;
        ss << std::hex;
        for (int j = 0; j < 4; j++)
        {
            ss << "\\x" << std::setw(2) << std::setfill('0')
               << ((c >> j * 8) & 0xff);
        }
    }
    std::cout << "printf \"" << ss.str() << "\"" << std::endl;
    return 0;
}
