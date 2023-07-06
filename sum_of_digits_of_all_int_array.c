// Skillrack
// Sum of digits of all integers in an array

int allDigitSum(int *arr, int LENGTH)
{
    int sum = 0;
    for(int i=0; i<LENGTH; i++){
        while(arr[i] > 0){
            int temp = arr[i]%10;
            sum += temp;
            arr[i]/=10;
        }
    }
    return sum;
}
