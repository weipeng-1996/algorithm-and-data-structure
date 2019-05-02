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
	void create(int n);//β�巨
	//void create1(int n);//ͷ�巨
	int get_length() { return length; }
	Node* get_node(int index);//��ȡ��indexλ�õ�ֵ
	int check_element(int element);//����������Ƿ���element���ֵ,���з�������������û�з���0
	void insert(int x, int index);//��x �����indexλ��
	void insert1(int x);//������β����ʼ����1��Ԫ��
	bool isempty() { return (length == 0); }//
	void dele(int index);//ɾ����indexλ�õ�Ԫ��
	void print();//�����ӡ����
	void print1();//�����ӡ
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
		cout << "��λ�ò�����" << endl;
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
		cout << "��λ�ò�����" << endl;
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