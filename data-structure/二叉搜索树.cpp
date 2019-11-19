#include<iostream>
using namespace std;

struct Node
{
	int value;
	Node *parent;
	Node *left;
	Node *right;
	int depth;//深度
	Node(int x):value(x), depth(0),left(NULL), right(NULL),parent(NULL){}
};


class BinarySearchTree
{

private:
	Node *root;

public:
	BinarySearchTree();
	~BinarySearchTree();
	void insert_node(Node* new_node, Node* &cur, Node* parent);//用于递归实现 insert(int x)
	void insert_node(int x);// 插入X值
	void delete_node(int x);// 查找若有X则删除X，若没有则输出没有该节点
	//void change_node(int a, int b);
	Node* search_node(int x);//查找元素X并返回该节点,非递归实现
	Node* search_node(Node *cur, int x);//递归实现search
	Node* search(int x);
	void destroy_tree(Node* &cur);//DELETE树
	void destroy() {
		destroy_tree(root);
	}
	void pre_print_tree(Node *cur);//打印,前序遍历
	void pre_print_tree();
	void in_print_tree(Node *cur);//中序遍历
	void in_print_tree();
	void post_print_tree(Node *cur);//后序遍历
	void post_print_tree();
	bool is_empty() {
		return root == NULL;
	}
	// 获取孩子个数
	int get_child_num(Node *cur) {
		if (cur == NULL)
			return -1;
		else if (cur->left == NULL && cur->right == NULL)
			return 0;
		else if ((cur->left == NULL && cur->right != NULL) || (cur->left != NULL && cur->right == NULL))
			return 1;
		else
			return 2;
	}
	//获得最小节点
	Node* get_min_node(Node* cur) {
		if (cur->left == NULL) {
			return cur;
		}
		else {
			get_min_node(cur->left);
		}
	}
};

BinarySearchTree::BinarySearchTree()
{
	root = NULL;
}

BinarySearchTree::~BinarySearchTree()
{
}

// p为当前节点， new_node为待插入节点
void BinarySearchTree::insert_node(Node* new_node, Node* &cur, Node* parent) {
	
	if (cur == NULL) {
		new_node->parent = parent;
		if (new_node->value < parent->value) {
			parent->left = new_node;
		}
		else {
			parent->right = new_node;
		}
	}
	else {
		if (new_node->value == cur->value) {
			cout << "树中已经存在该节点无法插入!" << endl;
			return;
		}
		if (new_node->value < cur->value) {
			new_node->depth++;
			insert_node(new_node, cur->left, cur);
			return;
		}
		if (new_node->value > cur->value) {
			new_node->depth++;
			insert_node(new_node, cur->right, cur);
			return;
		}
	}
}

void BinarySearchTree::insert_node(int x) {
	Node *new_node = new Node(x);
	if (root == NULL) {
		root = new_node;
		return;
	}
	insert_node(new_node, root, NULL);
}

void BinarySearchTree::pre_print_tree(Node *cur) {
	if (cur != NULL) {
		cout << cur->value<<" ";
		pre_print_tree(cur->left);
		pre_print_tree(cur->right);
	}
}

void BinarySearchTree::pre_print_tree() {
	if (is_empty()) {
		cout << "空树" << endl;
	}
	pre_print_tree(root);
}

void BinarySearchTree::in_print_tree() {
	if (is_empty()) {
		cout << "空树" << endl;
	}
	in_print_tree(root);
}

void BinarySearchTree::in_print_tree(Node *cur) {
	if (cur != NULL) {
		in_print_tree(cur->left);
		cout << cur->value << " ";
		in_print_tree(cur->right);
	}
}

void BinarySearchTree::post_print_tree() {
	if (is_empty()) {
		cout << "空树" << endl;
	}
	post_print_tree(root);
}

void BinarySearchTree::post_print_tree(Node *cur) {
	if (cur != NULL) {
		post_print_tree(cur->left);
		post_print_tree(cur->right);
		cout << cur->value << " ";
	}
}

void BinarySearchTree::destroy_tree(Node* &cur) {
	if (cur == NULL) {
		cout << "该树为空" << endl;
		return;
	}
	if (cur->left != NULL)
		destroy_tree(cur->left);
	if (cur->right != NULL)
		destroy_tree(cur->right);
	delete cur;
	cur = NULL;
}

Node* BinarySearchTree::search_node(int x) {
	Node *cur = root;
	while (cur != NULL) {
		if (x == cur->value) {
			return cur;
		}
		else if (x < cur->value) {
			cur = cur->left;
		}
		else {
			cur = cur->right;
		}
	}
	cout << "树中无此值" << endl;
	return NULL;
}

Node* BinarySearchTree::search(int x) {
	return search_node(root, x);
}

Node* BinarySearchTree::search_node(Node *cur, int x) {
	if (cur == NULL) {
		cout << "树中无此值" << endl;
		return NULL;
	}
	else if (x == cur->value) {
		return cur;
	}
	else if (x < cur->value) {
		search_node(cur->left, x);
	}
	else {
		search_node(cur->right, x);
	}
}

void BinarySearchTree::delete_node(int x) {
	Node * cur = search_node(x);
	if (cur == NULL) {
		cout << "无此节点，删除失败" << endl;
	}
	// 待删除节点无子节点
	else if (get_child_num(cur)==0) {
		if (cur->value = cur->parent->left->value) {
			cur->parent->left = NULL;
		}
		else {
			cur->parent->right = NULL;
		}
	}
	//待删除节点有1个子节点
	else if (get_child_num(cur) == 1) {
		//待删除节点为根节点
		if (cur == root) {
			if (cur->left != NULL) {
				delete root;
				root = cur->left;
				return;
			}
			else {
				delete root;
				root = cur->right;
				return;
			}
		}
		else {
			if (cur->left != NULL) {
				cur->left->parent = cur->parent;
				if (cur == cur->parent->left)
					cur->parent->left = cur->left;
				else
					cur->parent->right = cur->left;
				cur->left->depth--;
			}
			else {
				cur->right->parent = cur->parent;
				if (cur == cur->parent->right)
					cur->parent->right = cur->right;
				else
					cur->parent->left = cur->right;
				cur->right->depth--;
			}
		}
	}
	// 待删除节点有两个子节点
	else if (get_child_num(cur) == 2) {
		// 获取待删除节点右子树的最小节点
		Node* temp = get_min_node(cur->right);
		// 存值右子树的最小节点
		int temp_value = temp->value;
		// 删除右子树的最小节点
		delete_node(temp_value);
		//将右子树的最小节点的值赋给待删除节点
		cur->value = temp_value;
		return;
	}
	delete cur;
}

int main() {
	BinarySearchTree Tree;
	Tree.insert_node(12);
	Tree.insert_node(5);
	Tree.insert_node(15);
	Tree.insert_node(3);
	Tree.insert_node(7);
	Tree.insert_node(1);
	Tree.insert_node(9);
	Tree.insert_node(8);
	Tree.insert_node(11);
	Tree.insert_node(13);
	Tree.insert_node(17);
	Tree.insert_node(16);
	Tree.insert_node(14);
	Tree.insert_node(20);
	Tree.insert_node(18);
	Tree.pre_print_tree();
	cout << endl;
	Tree.delete_node(12);
	Tree.pre_print_tree();
	cout << endl;
	cout << Tree.search(8);
	Tree.destroy();
	Tree.destroy();
	if (Tree.is_empty())
		cout << "TRUE" << endl;
}