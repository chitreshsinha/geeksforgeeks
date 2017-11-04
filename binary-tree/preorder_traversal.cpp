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
	return head;
}

void printPreorder(struct node *head) {
	if (head == NULL) {
		return;
	}
	cout << head->data << " - ";
	printPreorder(head->left);
	printPreorder(head->right);
}

int main() {
	printPreorder(createTree());
	cout << endl;
	return 0;
}
