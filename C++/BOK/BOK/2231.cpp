#include <iostream>

int main() {
	int st;
	int result = 0;
	scanf("%d", &st);
	result += st;
	while (st > 10) {
		result += st % 10;
		st = 10;
		printf("%d\n", st);
	}
	printf("%d", result);
}