#include <stdio.h>
void ThreeFive(int x) {
  if( x % 3 ==0 and x % 5==0){
  	printf("ThreeFive\n");
  }
  else if(x % 3 ==0 ){
  		printf("Three\n");
  }
  else if(x%5 ==0 ){
  	printf("Five\n");
  }
  else{
  	printf("%d\n",x);
  }
}

int main(){
	int i;
	for(i=1; i<=100; i++){
		ThreeFive(i);
	}
	

}


