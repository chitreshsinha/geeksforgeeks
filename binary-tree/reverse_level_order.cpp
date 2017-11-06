#include <iostream>

using namespace std;

struct node {
	int data;
	struct node *left;
	struct node *right;
};

struct node* newNode(int data) {
	struct node *head = NULL;
	head = new node();
	head->data = data;
	head->left = NULL;
	head->right = NULL;
	return head;
} 

struct node* createTree() {
	struct node *head = newNode(1);
	head->left = newNode(2);
	head->right = newNode(3);
	head->left->left = newNode(4);
	head->left->right = newNode(5);
	head->left->right->left = newNode(7);
	head->left->right->right = newNode(8);
	head->right->right = newNode(6);
	head->right->right->left = newNode(9);
	return head;
}

int getHeight(struct node *head) {
	if (head==NULL) {
		return 0;
	} else {
		int lHeight = getHeight(head->left) + 1;
		int rHeight = getHeight(head->right) + 1;
		return max(lHeight, rHeight);
	}
}

void printLevel(struct node *head, int level) {
	if (head == 0) {
		return;
	}
	if (level == 1) {
		cout << head->data << " ";
	} else {
		printLevel(head->left, level-1);
		printLevel(head->right, level-1);
	}
}

void printLevelOrderLine(struct node *head) {
	int height = getHeight(head);
	int i;
	for (i=height;i>=1;i--) {
		printLevel(head, i);
		cout << endl;
	}
}

int main() {
	struct node *head = createTree();
	printLevelOrderLine(head);
}