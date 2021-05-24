#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;

long int caluclate_fibonacci(long int n){
    if (n==0){
        return 0;
    }
    else if (n==1 || n==2){
        return 1;
    }
    long int first=0, second=1, nth;
    for(int i=2;i<=n;i++){
        nth = first + second;
        first = second;
        second = nth;
    }
    return second;
}

int main(){
    long int n = 3;
    cout << "Enter n:";
    cin >> n;
    long int res = caluclate_fibonacci(n);
    cout << n << "th Fibonacci number = " << res << endl;
    return 0;
}