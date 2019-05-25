#include<iostream>
using namespace std;

struct Node
{
	int value;
	Node *parent;
	Node *left;
	Node *right;
	int depth;//���
	Node(int x):value(x), depth(0),left(NULL), right(NULL),parent(NULL){}
};


class BinarySearchTree
{

private:
	Node *root;

public:
	BinarySearchTree();
	~BinarySearchTree();
	void insert_node(Node* new_node, Node* &cur, Node* parent);//���ڵݹ�ʵ�� insert(int x)
	void insert_node(int x);// ����Xֵ
	void delete_node(int x);// ��������X��ɾ��X����û�������û�иýڵ�
	//void change_node(int a, int b);
	Node* search_node(int x);//����Ԫ��X�����ظýڵ�,�ǵݹ�ʵ��
	Node* search_node(Node *cur, int x);//�ݹ�ʵ��search
	Node* search(int x);
	void destroy_tree(Node* &cur);//DELETE��
	void destroy() {
		destroy_tree(root);
	}
	void pre_print_tree(Node *cur);//��ӡ,ǰ�����
	void pre_print_tree();
	void in_print_tree(Node *cur);//�������
	void in_print_tree();
	void post_print_tree(Node *cur);//�������
	void post_print_tree();
	bool is_empty() {
		return root == NULL;
	}
	// ��ȡ���Ӹ���
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
	//�����С�ڵ�
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

// pΪ��ǰ�ڵ㣬 new_nodeΪ������ڵ�
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
			cout << "�����Ѿ����ڸýڵ��޷�����!" << endl;
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
		cout << "����" << endl;
	}
	pre_print_tree(root);
}

void BinarySearchTree::in_print_tree() {
	if (is_empty()) {
		cout << "����" << endl;
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
		cout << "����" << endl;
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
		cout << "����Ϊ��" << endl;
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
	cout << "�����޴�ֵ" << endl;
	return NULL;
}

Node* BinarySearchTree::search(int x) {
	return search_node(root, x);
}

Node* BinarySearchTree::search_node(Node *cur, int x) {
	if (cur == NULL) {
		cout << "�����޴�ֵ" << endl;
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
		cout << "�޴˽ڵ㣬ɾ��ʧ��" << endl;
	}
	// ��ɾ���ڵ����ӽڵ�
	else if (get_child_num(cur)==0) {
		if (cur->value = cur->parent->left->value) {
			cur->parent->left = NULL;
		}
		else {
			cur->parent->right = NULL;
		}
	}
	//��ɾ���ڵ���1���ӽڵ�
	else if (get_child_num(cur) == 1) {
		//��ɾ���ڵ�Ϊ���ڵ�
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
	// ��ɾ���ڵ��������ӽڵ�
	else if (get_child_num(cur) == 2) {
		// ��ȡ��ɾ���ڵ�����������С�ڵ�
		Node* temp = get_min_node(cur->right);
		// ��ֵ����������С�ڵ�
		int temp_value = temp->value;
		// ɾ������������С�ڵ�
		delete_node(temp_value);
		//������������С�ڵ��ֵ������ɾ���ڵ�
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