#include <iostream>

// -------------------------------------
int* quicksort(int*, int, int);
int partition(int* , int, int);
// --------------------------------------
int partition(int* arr, int end, int start)
{
    int p = (end + start) / 2, i = start, j = end;
    while(i < j){
        while(arr[i] < arr[p]) i += 1;
        while(arr[j] > arr[p]) j -= 1;
        if(i >= j) break;
        std::swap(arr[i++], arr[j--]);
    }
    return p;
}

int* quicksort(int* arr, int end, int start)
{
    if(start < end){
        int p = partition(arr, end, start);
        quicksort(arr, p,  start);
        quicksort(arr, end, p + 1);
    }
    return arr;
}

int main()
{
    int arr[1000] = {0}, num;
    int*  arr_sorted;
    std::cin >> num;
    for(int i = 0; i < num; i++)
    {
        std::cin >> arr[i];
    }
    arr_sorted = quicksort(arr, num - 1, 0);
    for(int i = 0; i < num; i++)
    {
        std::cout << arr_sorted[i] << ' ';
    }
}