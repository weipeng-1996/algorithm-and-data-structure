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
	void create(int n);				//尾插法
	void create1(int n);			//头插法
	int get_element(int index);		//获取第index位置的值
	int check_element(int element); //检查链表中是否有element这个值,若有返回其索引，若没有返回0
	void insert(int x, int index);  //将x 插入第index位置
	bool isempty();					//
	void dele(int index);			//删除第index位置的元素
	void print();					//打印链表
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
		cout << "表为空" << endl;
		return -1;
	}
	if (length < index) {
		cout << "该位置不存在" << endl;
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
		cout << "表为空" << endl;
		return;
	}
	if (length < index ||index<=0) {
		cout << "该位置不存在" << endl;
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
		cout << "位置异常" << endl;
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