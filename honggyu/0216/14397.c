//#define _CRT_SECURE_NO_WARNINGS
//#include<stdio.h>
//#include<stdlib.h>
//
//int main() {
//	// rows : 세로 / cols : 가로
//	int rows, cols;
//
//	scanf("%d %d", &rows, &cols);
//
//	printf("%d %d", rows, cols);
//
//	char** grid = (char**)malloc(rows * sizeof(char*));
//
//
//
//
//	for (int i = 0;i < rows;i++) {
//		grid[i] = (char*)malloc((cols + 1) * sizeof(char));
//	}
//
//
//
//
//	for (int i = 0;i < rows;i++) {
//		scanf("%s", grid[i]);
//	}
//	
//	int allcnt = 0;
//
//	for (int i = 0;i < cols;i++) {
//		if (grid[0][i] == "#") {
//			try{
//				if (grid[0][i - 1] == ".") {
//					allcnt += 1;
//				}
//			}
//			except{
//
//			}
//		}
//	}
//
//	for (int i = 0;i < rows-1;i++) {
//		int flag = 0;
//		if (i % 2 != 0) {
//			flag = 1;
//		}
//
//
//	}
//
//
//
//	for (int i = 0; i < rows; i++) {
//		printf("%s\n",grid[i]);
//	}
//
//	// 동적 할당 해제
//	for (int i = 0; i < rows; i++) {
//		free(grid[i]); // 각 행에 대한 메모리 해제
//	}
//	free(grid); // 2차원 배열에 대한 메모리 해제
//
//	return 0;
//
//
//
//
//}
//
//
//
//
//
//
