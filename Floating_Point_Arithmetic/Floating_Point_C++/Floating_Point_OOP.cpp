// A better approach using Object Oriented Programming

#include <iostream>
#include <array>

template <size_t N>
class Float {
public:
    int front;
    std::array<char, N> back;
    Float(int tmp1, std::array<char, N> tmp2) {
        front = tmp1;
        back = tmp2;
    }
    void display() {
        std::cout << front << '.';
        for (int i = 0; i < N; i++) {
            std::cout << back[i];
        }
        std::cout << "\n";
    }
    Float add(Float num) {
        int tmp1 = front + num.front;
        std::array<char, N> tmp2{'3', '4'};
        Float<N> out(tmp1, tmp2);
        return out;
    }
};



int main() {
    Float<2> num1(12, std::array<char, 2>{'3', '4'});
    Float<2> num2(56, std::array<char, 2>{'2', '2'});
    num1.display();

    Float sum = num1.add(num2);
    sum.display();
}