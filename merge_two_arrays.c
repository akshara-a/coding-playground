// Merge two arrays

#include <stdio.h>

int main()
{
    // First array
    int n;
    scanf("%d", &n); 
    int arr1[n];
    for(int i=0; i<n; i++)
        scanf("%d", &arr1[i]); 
    
    // Second array
    int m;
    scanf("%d", &m); 
    int arr2[m];
    for(int i=0; i<m; i++)
        scanf("%d", &arr2[i]); 
        
    // Merge arrays 
    int k; 
    k = n+m; 
    int arr[k];
    for(int i=0; i<n; i++){
        arr[i] = arr1[i]; 
    }
    for(int i=n; i<k; i++){
        arr[i] = arr2[((m+i)-k)]; 
    }
    
    // Newly formed array 
    for(int i=0; i<k; i++){
        printf("%d ", arr[i]); 
    }
    printf("\n--------------------\n");
    
    return 0;
}
