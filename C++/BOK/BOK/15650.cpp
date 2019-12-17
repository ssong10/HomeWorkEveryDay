#include <stdio.h>

int N, M;
int arr[8], rst[8];
bool v[8] = { false, };

void back(int n)
{
	if (n == M+1) {
		for (int i = 1; i < M + 1; i++) {
			printf("%d ", rst[i]);
		}
		printf("\n"); return;
	}
	for (int i = n; i < N + 1; i++) {
		if (!v[i]) {
			if (rst[n - 1] < i) {
				rst[n] = i; v[i] = true;
				back(n + 1);
				rst[n] = 0; v[i] = false;
			}
		}
	}

}

int main()
{
	scanf("%d %d", &N, &M);
	back(1);
}