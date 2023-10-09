#include <iostream>

// ---------------------------
int* mergesort(int*, int);
int* merge(int*, int*, int, int)
// ---------------------------

int* mergesort(int* arr, int num)
{
    int
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
    arr_sorted = mergesort(arr, num);
    for(int i = 0; i < num; i++)
    {
        std::cout << arr_sorted[i] << ' ';
    }
}