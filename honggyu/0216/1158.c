#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


int main() {
	int total, seq;

	scanf("%d %d", &total, &seq);

	int* numbers = (int*)malloc((total+1) * sizeof(int));
	int* answer = (int*)malloc(total * sizeof(int));

	for (int i = 1;i < total+1;i++) {
		numbers[i] = i;
	}
	numbers[0] = 0;


	int allcnt = 0;
	int pointer = 1;

	while (allcnt < total) {
		int cnt = 0;

		while (cnt < seq) {

			if (numbers[pointer] != 0) {
				cnt += 1;
				
			}



			if (cnt < seq) {
				if (pointer == total) {
					pointer = 1;
				}
				else {
					pointer += 1;
				}
			}
			else {
				break;
			}
		}

		//printf("allcnt : %d\n\n\n", allcnt);
		answer[allcnt] = numbers[pointer];
		numbers[pointer] = 0;
		allcnt += 1;


		
	}
	printf("<");
	for (int i = 0;i < total-1;i++) {
		printf("%d, ", answer[i]);
	}
	printf("%d", answer[total-1]);
	printf(">");


	return 0;
}







