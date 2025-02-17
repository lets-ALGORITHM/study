#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

int main() {

	int N;
	scanf("%d", &N);

	int** grid = (int**)malloc(N * sizeof(int*));

	long total = 0;
	for (int i = 0;i < N;i++) {
		grid[i] = (int*)malloc(N * sizeof(int));
	}

	for (int i = 0;i < N;i++) {
		for (int j = 0;j < N;j++) {
			scanf("%d", &grid[i][j]);
			total += grid[i][j];
		}
	}
	//for (int i = 0;i < N;i++) {
	//	for (int j = 0;j < N;j++) {
	//		printf("%d", grid[i][j]);
	//	}
	//	printf("\n");
	//}

	long cnt = 0;
	for (int k = 0;k < 10000000;k++) {
		for (int i = 0;i < N;i++) {
			for (int j = 0;j < N;j++) {
				if (grid[i][j] > 0) {
					cnt += 1;
					grid[i][j] -= 1;
				}
				
			}
		}
		//printf("grid\n");
		//for (int i = 0;i < N;i++) {
		//	for (int j = 0;j < N;j++) {
		//		printf("%d", grid[i][j]);
		//	}
		//	printf("\n");
		//}
		if (cnt >= (int)total / 2) {
			if (cnt == 0) {
				printf("%d", k);
				return 0;
			}
			printf("%d", k+1);
			return 0;
		}
	}
	





	return 0;
}