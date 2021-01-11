#include <bits/stdc++.h>
#define ll long long
#define ar array
#define pb push_back
#define vi vector<int>
#define vvi vector<vector<int>>
#define vii vector<int, int>
#define pii pair<int, int>

using namespace std;
const ll M = 1000000007;
const int mxN = 1e3;

void merge(int arr[], int l, int m, int r){

   int tmp[6];

   int i = l, left_end = m;
   int j = m + 1, right_end = r;
   int k = l;

   for (; i <= left_end && j <= right_end; k++){
       if (arr[i] < arr[j]){
           tmp[k] = arr[i];
           i++;
       }else{
           tmp[k] = arr[j];
           j++;
        }
   }

   while (i <= left_end){
       tmp[k] = arr[i];
       i++;
       k++;
   }

   while (j <= right_end){
       tmp[k] = arr[j];
       j++;
       k++;
   }

   for (int x = l; x < r+1; x++){
       arr[x] = tmp[x];
   }
    
}
 
// l is for left index and r is
// right index of the sub-array
// of arr to be sorted */
void mergeSort(int arr[],int l,int r){
    if(l>=r){
        return;//returns recursively
    }
    int m = (l+r-1)/2;
    mergeSort(arr,l,m);
    mergeSort(arr,m+1,r);
    merge(arr,l,m,r);
}
 
// UTILITY FUNCTIONS
// Function to print an array
void printArray(int A[], int size)
{
    for (int i = 0; i < size; i++)
        cout << A[i] << " ";
}
 
// Driver code
int main()
{
    int arr[] = { 12, 11, 13, 5, 6, 7 };
    int arr_size = sizeof(arr) / sizeof(arr[0]);
 
    cout << "Given array is \n";
    printArray(arr, arr_size);
 
    mergeSort(arr, 0, arr_size - 1);
 
    cout << "\nSorted array is \n";
    printArray(arr, arr_size);
    return 0;
}