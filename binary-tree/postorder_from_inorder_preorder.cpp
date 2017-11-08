#include <iostream>

using namespace std;

int search(int arr[], int num, int len) {
	int i = 0;
	for(i=0;i<len;i++) {
		if (arr[i] == num) {
			return i;
		}
	}
	return -1;
}

void printPostOrder(int in[], int pre[], int len) {
	int root = search(in, pre[0], len);
	if (root != 0) {
		printPostOrder(in, pre+1, root);
	}
	if (root != len-1) {
		printPostOrder(in+root+1, pre+root+1, len-root-1);
	}

	cout << pre[0] << " ";

}

int main() {
	int preOrder[] = {1, 2, 4, 5, 3, 6};
	int inOrder[] = {4, 2, 5, 1, 3, 6};
	int len = sizeof(preOrder)/sizeof(preOrder[0]);
	printPostOrder(inOrder, preOrder, len);
	cout << endl;
	return 0;
}