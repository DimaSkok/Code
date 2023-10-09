#include <iostream>
using namespace std;
int search_rec(int x, int* array, int n);
int search_rec(int x, int* array, int n){
    int st = 0;
    n -= 1;
    if(array[st] == x){
        return st;
    }
    if(array[n] == x){
        return n;
    }
    for(;n != st;){
        if(1 <= (n - st) && (n - st) <= 5){
            for(int i = st; i <= n; i++){
                if(array[i] == x){
                    return i;
                }
            }
            return -1;
        }
        if(array[(n - st)/2 + st] == x) {
            return ((n - st)/2 + st);
        }
        if(array[(n - st)/2 + st] < x) {
            st = (n - st)/2 + st;
        }
        else {
            n = (n - st)/2 + st;
        }
    }
    return -1;
}

int main()
{
    int n, a[100], x;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int i = 0; i < 5; i++)
    {
        cin >> x;
        cout << search_rec(x, a, n) << " ";
    }
    cout << endl;
    return 0;
}