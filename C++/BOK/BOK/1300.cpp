#include <stdio.h>
int main() {
	int N = 0;
	int k;
	scanf("%d", &N);
	scanf("%d", &k);
	int arr[10 ^ 5][10 ^ 5] = { 0, };
	int result[100] = { 0, };
	for (int y=0; y < N;  y++) {
		for (int x=0; x < N; x++) {
			printf("%d ", (y + 1)*(x + 1));

		}
		printf("\n");
	}

	int anw;
	for (int i = 0; i < sizeof(result)/4; i++) {
		if (k) {
			k -= result[i];
		}
		else {
			break;
		}
		anw = i;
	}
	printf("%d", anw);
}