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

void printLevelorder(queue<struct node *> q) {
	struct node *head = q.front();
	if (head != NULL) {
		cout << head->data << endl;
		q.pop();
		q.push(head->left);
		q.push(head->right);
		printLevelorder(q);		
	}
}

int getHeight(struct node *head) {
	if (head==NULL) {
		return 0;
	} else {
		int lDepth = getHeight(head->left) + 1;
		int rDepth = getHeight(head->right) + 1;
		return max(lDepth, rDepth);
	}
}

void printLevel(struct node *tree, int level) {
	if (tree == NULL) {
		return;
	} 
	if (level == 1) {
		cout << tree->data << endl;
	} else {
		printLevel(tree->left, level-1);
		printLevel(tree->right, level-1);
	}
}

void printLevelorder2(struct node *tree, int height) {
	int i=0;
	for (i=1;i<=height;i++) {
		printLevel(tree, i);
	}
}

int main() {
	queue <struct node *> q;
	struct node *head = createTree();
	q.push(head);
	int height = getHeight(head);
	printLevelorder(q);
	cout << "Print Level Order 2" << endl; 
	printLevelorder2(head, height);
	return 0;
}
