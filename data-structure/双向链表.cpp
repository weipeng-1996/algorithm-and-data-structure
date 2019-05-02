#include<iostream>
using namespace std;

struct Node {
	int data;
	Node *pre;
	Node *next;
	Node(int value, Node *pre, Node *next):data(value), pre(pre), next(next){}
};

class LinkList
{
private:
	Node *head;
	int length;
public:
	LinkList();
	//~LinkList();
	void create(int n);//尾插法
	//void create1(int n);//头插法
	int get_length() { return length; }
	Node* get_node(int index);//获取第index位置的值
	int check_element(int element);//检查链表中是否有element这个值,若有返回其索引，若没有返回0
	void insert(int x, int index);//将x 插入第index位置
	void insert1(int x);//从链表尾部开始插入1个元素
	bool isempty() { return (length == 0); }//
	void dele(int index);//删除第index位置的元素
	void print();//正序打印链表
	void print1();//倒序打印
};

LinkList::LinkList() {
	head = new Node(0, nullptr, nullptr);
	head->pre = head;
	head->next = head;
	length = 0;
}

void LinkList::create(int n) {
	Node *p;
	int data;
	for (int i = 0; i < n; i++) {
		cin >> data;
		p = new Node(data, head->pre, head);
		head->pre->next = p;
		head->pre = p;
		length++;
	}
}

Node* LinkList::get_node(int index) {
	if (index > length || index <= 0) {
		cout << "该位置不存在" << endl;
		return nullptr;
	}
	Node *p = head;
	if (index <= length / 2) {
		while (index) {
			p = p->next;
			index--;
		}
		return p;
	}
	else {
		index = length - index;
		p = p->pre;
		while (index) {
			p = p->pre;
			index--;
		}
		return p;
	}
}

int LinkList::check_element(int element) {
	Node *p = head;
	for (int i = 0; i < length; i++) {
		p = p->next;
		if (p->data == element)
			return i + 1;
	}
	return 0;
}

void LinkList::insert(int x, int index) {
	Node *p = get_node(index);
	Node *new_node = new Node(x, p->pre, p);
	p->pre = new_node;
	new_node->pre->next = new_node;
	length++;
}

void LinkList::insert1(int x) {
	Node *p = head->pre;
	Node *new_node = new Node(x, p, p->next);
	p->next = new_node;
	head->pre = new_node;
	length++;
}

void LinkList::dele(int index) {
	if (index > length || index <= 0) {
		cout << "该位置不存在" << endl;
		return;
	}
	Node *p = head;
	if (index <= length / 2) {
		while (index) {
			p = p->next;
			index--;
		}
		p->pre->next = p->next;
		p->next->pre = p->pre;
		delete p;
	}
	else {
		index = length - index;
		p = p->pre;
		while (index) {
			p = p->pre;
			index--;
		}
		p->pre->next = p->next;
		p->next->pre = p->pre;
		delete p;
	}
	length--;
}

void LinkList::print() {
	Node *p = head;
	for (int i = 0; i < length; i++) {
		p = p->next;
		if (i == length - 1) {
			cout << p->data << endl;
			break;
		}
		cout << p->data << " ";
	}
}

void LinkList::print1() {
	Node *p = head;
	for (int i = 0; i < length; i++) {
		p = p->pre;
		if (i == length - 1) {
			cout << p->data << endl;
			break;
		}
		cout << p->data << " ";
	}
}

int main() {
	LinkList l1;
	l1.create(6);
	l1.print();
	l1.print1();
	cout<<l1.get_length()<<endl;
	cout << l1.get_node(4)->data<< endl;
	l1.insert(99, 5);
	l1.print();
	l1.print1();
	l1.insert1(88);
	l1.print();
	l1.print1();
	l1.dele(6);
	l1.print();
	l1.print1();
}