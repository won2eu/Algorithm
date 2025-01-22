#include <stdio.h>

int hanoi(int n, char a, char b, char c);

int main(){
    int K;
    int L=1;
    scanf("%d",&K);

    for(int i=0; i<K; i++){
        L*=2;
    }
    printf("%d\n",L-1);

    hanoi(K,'1','2','3');

    return 0;


}

int hanoi(int n, char a, char b, char c){
    if(n==1) {
            printf("%c %c\n",a,c);
            return 0;
    }
    else{

        hanoi(n-1,a,c,b);

        printf("%c %c\n",a,c);

        hanoi(n-1,b,a,c);
    }
}
