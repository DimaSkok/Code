#include <iostream>

// ---------------------------------
int* grabesort(int*, int);
// ---------------------------------

int* grabesort(int* arr, int num)
{
    float  fact_inc = 1.247;
    int step = num / fact_inc;
    while(step >= 1) {
        for(int i = 0; i + step < num; i++){
            if(arr[i] > arr[i + step]){
                std::swap(arr[i], arr[i + step]);
            }
        }
        step /= fact_inc;
    }
    return arr;
}

int main()
{
    int arr[1000] = {0}, num;
    int* arr_sorted;
    std::cin >> num;
    for(int i = 0; i < num; i++)
    {
        std::cin >> arr[i];
    }
    arr_sorted = grabesort(arr, num);
    for(int i = 0; i < num; i++)
    {
        std::cout << arr_sorted[i] << ' ';
    }
}