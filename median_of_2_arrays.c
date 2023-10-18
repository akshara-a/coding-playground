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
    
    // Sort array 
    for(int i=0; i<k; i++){
        for(int j=i+1; j<k; j++){
            if(arr[i] > arr[j]){
                int temp = arr[i]; 
                arr[i] = arr[j]; 
                arr[j] = temp;
            }
        }
    }
    
    // Sorted array
    for(int i=0; i<k; i++){
        printf("%d ", arr[i]); 
    }
    printf("\n--------------------\n");
    
    // Median 
    if(k%2 != 0){
        int mid = k/2; 
        printf("Median is %d", arr[mid]); 
    }
    else{
        int m1 = k/2; 
        int m2 = m1-1; 
        float val = (arr[m1]+arr[m2])/2.0; 
        printf("Median is %.2f", val); 
    }

    
    return 0;
}
