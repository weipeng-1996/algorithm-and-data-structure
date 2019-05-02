#include<iostream>
using namespace std;

struct Node {
	int data;
	Node *next;
};

class LinkList
{
private:
	Node *head;
	int length;
public:
	LinkList();
	~LinkList();
	void create(int n);//β�巨
	void create1(int n);//ͷ�巨
	int get_element(int index);//��ȡ��indexλ�õ�ֵ
	int check_element(int element);//����������Ƿ���element���ֵ,���з�������������û�з���0
	void insert(int x, int index);//��x �����indexλ��
	bool isempty();//
	void dele(int index);//ɾ����indexλ�õ�Ԫ��
	void print();//��ӡ����
};

LinkList::LinkList()
{
	head = new Node;
	head->next = NULL;
	length = 0;
}

LinkList::~LinkList()
{
	Node *p;
	while (head!=NULL) {
		p = head->next;
		delete head;
		head = p;
	}
}

void LinkList::create(int n) {
	Node *p, *r;
	r = head;
	for (int i = 0; i < n; i++) {
		p = new Node;
		cin >> p->data;
		r->next = p;
		r = p;
		length++;
	}
	r->next = NULL;
}

void LinkList::create1(int n) {
	Node *p;
	for (int i = 0; i < n; i++) {
		p = new Node;
		cin >> p->data;
		p->next = head->next;
		head->next = p;
		length++;
	}
}

bool LinkList::isempty() {
	return (head->next == NULL);
}

int LinkList::get_element(int index) {
	if (isempty()) {
		cout << "��Ϊ��" << endl;
		return -1;
	}
	if (length < index) {
		cout << "��λ�ò�����" << endl;
		return -1;
	}
	Node *p = head;
	for (int i = 0; i < index; i++) {
		p = p->next;
	}
	return p->data;
}

int LinkList::check_element(int element) {
	Node *p = head;
	for (int i = 0; i < length; i++) {
		p = p->next;
		if (p->data == element) {
			return (i + 1);
		}
		if (p->next == NULL)
			break;
	}
	return 0;
}

void LinkList::dele(int index) {
	if (isempty()) {
		cout << "��Ϊ��" << endl;
		return;
	}
	if (length < index ||index<=0) {
		cout << "��λ�ò�����" << endl;
		return;
	}
	Node *p = head;
	for (int i = 0; i < index-1; i++) {
		p = p->next;
	}
	Node *r = p;
	p = p->next;
	r->next = p->next;
	delete p;
	length--;
}

void LinkList::insert(int x, int index) {
	if (length+1 < index||index <= 0) {
		cout << "λ���쳣" << endl;
		return;
	}
	Node *p = head;
	for (int i = 0; i < index - 1; i++) {
		p = p->next;
	}
	Node *r = p->next;
	Node *n = new Node;
	n->data = x;
	p->next = n;
	n->next = r;
	length++;
}

void LinkList::print() {
	Node *p = head;
	for (int i = 0; i < length; i++) {
		p = p->next;
		cout << p->data << " ";
		if (p->next == NULL)
			break;
	}
}

int main() {
	LinkList l0 = LinkList();
	LinkList l1 = LinkList();
	cout << l0.check_element(5) << endl;
	cout << l0.get_element(10) << endl;
	l0.insert(5, 1);
	l0.print();
	l1.create(8);
	l1.print();
	cout << endl;
	l1.dele(8);
	l1.print();
	cout << endl;
	l1.dele(0);
	l1.insert(9, 9);
	l1.print();
}