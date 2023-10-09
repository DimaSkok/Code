#include <iostream>

// --------------------------------------
int* quicksort(int*, int, int);
// --------------------------------------

int* quicksort(int* arr, int end, int start)
{
    for(int i = start, i < end; i++){
        
    }
}

int main()
{
    int arr[1000] = {0}, num, arr_sorted[];
    std::cin >> num;
    for(int i = 0; i < num; i++)
    {
        std::cin >> arr[i];
    }
    arr_sorted = quicksort(arr, num, 0)
    for(int i = 0; i < num; i++)
    {
        std::cout << arr_sorted[i] << ' ';
    }
}