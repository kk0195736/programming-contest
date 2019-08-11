#include<iostream>
using namespace std;
int main()
{
    int A, B, C;
    cin >> A >> B >> C;

    if (A <= B+C){
        cout << B+C-A << endl;
    }else{
        cout << 0 << endl;
    }

    return 0;
}