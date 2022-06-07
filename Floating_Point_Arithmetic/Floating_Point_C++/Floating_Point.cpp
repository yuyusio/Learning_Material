////////////////////////////////////////////////////////////////////////////
// C++ floating point has a precision of only 6
// Arithmetic Operations past 6 digits is impossible
// As it only produces erroneous results

// Code written by yuyusio
////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <array>
#include <cstring>
#include <cmath>

std::array<int,2> add_dec(std::array<int,2> num1, std::array<int,2> num2) {
    int num_front = num1[0] + num2[0];
    int num_back = 0;

    char num1_char[9];
    char num2_char[9];
    sprintf(num1_char,"%i",num1[1]);
    sprintf(num2_char,"%i",num2[1]);
    const char *num1_ptr = num1_char;
    const char *num2_ptr = num2_char;
    const int num1_len = strlen(num1_ptr);
    const int num2_len = strlen(num2_ptr);

    if (num1_len > num2_len) {
        const int dif = num1_len - num2_len;
        num_back = num1[1] + num2[1] * pow(10,dif);

        char num_back_char[1];
        sprintf(num_back_char,"%i",num_back);
        const char *num_back_char_ptr = num_back_char;
        const int num_back_len = strlen(num_back_char_ptr);

        if (num_back_len > num1_len) {
            num_front++;
            num_back -= pow(10,num_back_len-1);
        }
    }

    else if (num2_len > num1_len) {
        const int dif = num2_len - num1_len;
        num_back = num2[1] + num1[1] * pow(10,dif);

        char num_back_char[1];
        sprintf(num_back_char,"%i",num_back);
        const char *num_back_char_ptr = num_back_char;
        const int num_back_len = strlen(num_back_char_ptr);

        if (num_back_len > num1_len) {
            num_front++;
            num_back -= pow(10,num_back_len-1);
        }
    }

    else {
        num_back = num1[1] + num2[1];

        char num_back_char[1];
        sprintf(num_back_char,"%i",num_back);
        const char *num_back_char_ptr = num_back_char;
        const int num_back_len = strlen(num_back_char_ptr);

        if (num_back_len > num1_len) {
            num_front++;
            num_back -= pow(10,num_back_len-1);
        }
    }

    std::array<int,2> output{num_front,num_back};
    return output;
}


int main() {
    std::cout.precision(20);
    std::cout << "\033[31m" << "Normal C++ arithmetic operation: " << "\033[0m" << "\n";
    std::cout << 12242.523 + 2332.9673 << "\n";

    std::cout << "\033[34m" << "Modified arithmetic operation: " << "\033[0m" << "\n";
    std::array<int,2> num1{12242,523};
    std::array<int,2> num2{2332,9673};
    std::array<int,2> sum{add_dec(num1,num2)};

    std::cout << sum[0] << '.' << sum[1] << "\n";

    return 0;
}