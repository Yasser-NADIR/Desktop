#include <stdio.h>
#include <stdlib.h>

int triPascal(int n, int p, int**mem){
    if(mem==NULL){
        mem = (int**)malloc(sizeof(int*)*n+1);
        int i, j;
        for(i=0;i<=n; i++){
            mem[i] = (int *)malloc(sizeof(int )*(i+1));
            for(j=0; j<i; j++){
                mem[i][j] = -1;
            }
        }
        mem[0][0]=1;
        mem[1][0]=1;
        mem[1][1]=1;

    }
    if(n<0 || p>n || p<0) return 0;
    if(n==0 || n==1) return 1;
    if(mem[n][p]!=-1) return mem[n][p];
    int val = triPascal(n-1, p, mem)+triPascal(n-1, p-1, mem);
    mem[n][p] = val;
    return val;
}



int main()
{
    int a = triPascal(4, 2, NULL);
    printf("la valeur est: %d\n",a);
    return 0;
}
