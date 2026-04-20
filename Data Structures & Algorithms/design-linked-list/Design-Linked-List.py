1class Node:
2    def __init__(self, val):
3        self.val = val
4        self.next = None
5
6
7class MyLinkedList:
8
9    def __init__(self):
10        self.head = None
11        self.length = 0
12
13    def get(self, index: int) -> int:
14        if index < 0 or index >= self.length:
15            return -1
16
17        curr = self.head
18        for _ in range(index):
19            curr = curr.next
20        return curr.val
21
22    def addAtHead(self, val: int) -> None:
23        node = Node(val)
24        node.next = self.head
25        self.head = node
26        self.length += 1
27
28    def addAtTail(self, val: int) -> None:
29        node = Node(val)
30
31        if not self.head:
32            self.head = node
33        else:
34            curr = self.head
35            while curr.next:
36                curr = curr.next
37            curr.next = node
38
39        self.length += 1
40
41    def addAtIndex(self, index: int, val: int) -> None:
42        if index < 0 or index > self.length:
43            return
44
45        if index == 0:
46            self.addAtHead(val)
47            return
48
49        if index == self.length:
50            self.addAtTail(val)
51            return
52
53        node = Node(val)
54        curr = self.head
55
56        for _ in range(index - 1):
57            curr = curr.next
58
59        node.next = curr.next
60        curr.next = node
61        self.length += 1
62
63    def deleteAtIndex(self, index: int) -> None:
64        if index < 0 or index >= self.length:
65            return
66
67        if index == 0:
68            self.head = self.head.next
69        else:
70            curr = self.head
71
72            for _ in range(index - 1):
73                curr = curr.next
74
75            curr.next = curr.next.next
76
77        self.length -= 1
78