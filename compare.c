#include <stdio.h>


int main(void)
{
	int a,b;
	scanf("%d %d",&a,&b);
	if (a>b){
		printf("A");
	}
	else if (b>a){
		printf("B");
	}
	else{
		printf("same");
	}
	return 0;
}