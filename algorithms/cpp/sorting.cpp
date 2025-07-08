#include <iostream>
#include <vector>
using namespace std;

void bubbleSortIter(vector<int>& array) {     // O(n^2)
    int n = array.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (array[j] > array[j + 1]) {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}

void bubbleSortRec(vector<int>& array, int i = -1) {     // O(n^2)
    if (i == -1) {
        i = array.size();
    }
    if (i <= 1) {
        return;
    }
    for (int j = 0; j < i - 1; ++j) {
        if (array[j] > array[j + 1]) {
            swap(array[j], array[j + 1]);
        }
    }
    bubbleSortRec(array, i - 1);
}

void selectionSortIter(vector<int>& array) {     // O(n^2)
    int n = array.size();
    for (int i = n - 1; i >= 0; --i) {
        int maxNumIndex = i;
        for (int j = 0; j <= i; ++j) {
            if (array[j] > array[maxNumIndex]) {
                maxNumIndex = j;
            }
        }
        swap(array[i], array[maxNumIndex]);
    }
}

int _prefixMax(vector<int>& array, int i) {
    if (i == 0) {
        return 0;
    }
    int j = _prefixMax(array, i - 1);
    if (array[j] > array[i]) {
        return j;
    }
    else {
        return i;
    }
}

void selectionSortRec(vector<int>& array, int i = -1) {     // O(n^2)
    if (i == -1) {
        i = array.size() - 1;
    }
    if (i > 0) {
        int j = _prefixMax(array, i);
        swap(array[i], array[j]);
        selectionSortRec(array, i - 1);
    }
}

void insertionSortIter(vector<int>& array) {     // O(n^2)
    for (int i = 1; i < array.size(); ++i) {
        int key = array[i];
        int j = i - 1;
        while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            --j;
        }
        array[j + 1] = key;
    }
}

void _insertLast(vector<int>& array, int i) {
    if (i > 0 && array[i] < array[i - 1]) {
        swap(array[i], array[i - 1]);
        _insertLast(array, i - 1);
    }
}

void insertionSortRec(vector<int>& array, int i = -1) {     // O(n^2)
    if (i == -1) {
        i = array.size() - 1;
    }
    if (i > 0) {
        insertionSortRec(array, i - 1);
        _insertLast(array, i);
    }
}

void _merge(const vector<int>& left, const vector<int>& right, vector<int>& array, int len_left, int len_right, int l, int r) {
    if (l < r) {
        if (len_right <= 0 || (len_left > 0 && left[len_left - 1] > right[len_right - 1])) {
            array[r - 1] = left[len_left - 1];
            _merge(left, right, array, len_left - 1, len_right, l, r - 1);
        } 
        else {
            array[r - 1] = right[len_right - 1];
            _merge(left, right, array, len_left, len_right - 1, l, r - 1);
        }
    }
}

void mergeSortRec(vector<int>& array, int l = 0, int r = -1) {     // O(nlogn)
    if (r == -1)
        r = array.size();
    if (1 < r - l) {
        int m = (l + r + 1) / 2;
        mergeSortRec(array, l, m);
        mergeSortRec(array, m, r);
        vector<int> left(array.begin() + l, array.begin() + m);
        vector<int> right(array.begin() + m, array.begin() + r);
        _merge(left, right, array, left.size(), right.size(), l, r);
    }
}