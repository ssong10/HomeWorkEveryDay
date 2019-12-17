// hsb.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//
#include <iostream>



int main()
{
	int arr[3][3][4] = { {{2,3,4},{3,4,5},{4,5,6}},{{5,6,7},{6,7,8},{7,8,9}} };
	printf("%d\n",arr[0][1][1]);
	for (int i = 0; i < 2; i++)
		for (int x = 0; x < 3; x++) {
			for (int y = 0; y < 3; y++) {
				if (i == 0) {
					arr[1][x][y] = arr[1][x][y] + arr[0][x][y];
				}
				printf("%d ", arr[i][x][y]);
			}
			printf("\n");
		}
	printf("\n");
}
