#include <stdio.h>

int N, M;
int num[9], rst[9] = { 0, };
bool visit[9] = { false, };
void back(int left)
{
	if (left == M+1) {
		for (int i = 0; i < M+1; i++) {
			if (rst[i])
				printf("%d ", rst[i]);
		}
		printf("\n");
		return;
	}
	for (int i = 1; i <= N; i++)
		if (!visit[i]) {
			rst[left] = i;
			visit[i] = true;
			back(left + 1);
			visit[i] = false;
			rst[left] = 0;
		}
}


int main()
{
	scanf("%d %d", &N, &M);
	back(1);
}