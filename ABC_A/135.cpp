#include<iostream>
using namespace std;
int main()
{
    int A, B;
    cin >> A >> B;
    if (A % 2 != B % 2){
        cout << "IMPOSSIBLE" << endl;
    }else{
        cout << (A + B) / 2 << endl;
    }
    return 0;
}