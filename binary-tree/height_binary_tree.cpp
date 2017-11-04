#include <iostream>
#include <queue>

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

int maxDepth(struct node *head) {
	if (head==NULL) {
		return 0;
	} else {
		int lDepth = maxDepth(head->left) + 1;
		int rDepth = maxDepth(head->left) + 1;
		return max(lDepth, rDepth);
	}
}

int main() {
	struct node *head = createTree();
	int height = maxDepth(head);
	cout << "Height: " << height << endl;
	return 0;
}
