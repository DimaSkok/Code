#include <iostream>
#include <vector>

std::vector<int> quicksort(std::vector<int>& arr) {
    if (arr.size() <= 1) {
        return arr;
    }
    int pivot = arr[arr.size() / 2];
    std::vector<int> left, middle, right;
    for (int x : arr) {
        if (x < pivot) {
            left.push_back(x);
        } else if (x == pivot) {
            middle.push_back(x);
        } else {
            right.push_back(x);
        }
    }
    std::vector<int> sorted_left = quicksort(left);
    std::vector<int> sorted_right = quicksort(right);

    std::vector<int> sorted_arr;
    sorted_arr.reserve(sorted_left.size() + middle.size() + sorted_right.size());
    
    sorted_arr.insert(sorted_arr.end(), sorted_left.begin(), sorted_left.end());
    sorted_arr.insert(sorted_arr.end(), middle.begin(), middle.end());
    sorted_arr.insert(sorted_arr.end(), sorted_right.begin(), sorted_right.end());

    return sorted_arr;
}

int main() {
    std::vector<int> my_vector = {5, 2, 9, 1, 7};
    
    std::vector<int> sorted_vector = quicksort(my_vector);

    for (int x : sorted_vector) {
        std::cout << x << " ";
    }
    
    return 0;
}