1class Node:
2    def __init__(self, url):
3        self.url = url
4        self.prev = None
5        self.next = None
6
7
8class BrowserHistory:
9    def __init__(self, homepage: str):
10        self.head = self.curr = Node(homepage)
11
12    def visit(self, url: str) -> None:
13        node = Node(url)
14
15        self.curr.next = None
16
17        self.curr.next = node
18        node.prev = self.curr
19        self.curr = node
20
21    def back(self, steps: int) -> str:
22        while steps and self.curr.prev:
23            steps -= 1
24            self.curr = self.curr.prev
25        return self.curr.url
26
27    def forward(self, steps: int) -> str:
28        while steps and self.curr.next:
29            steps -= 1
30            self.curr = self.curr.next
31        return self.curr.url
32
33
34# Your BrowserHistory object will be instantiated and called as such:
35# obj = BrowserHistory(homepage)
36# obj.visit(url)
37# param_2 = obj.back(steps)
38# param_3 = obj.forward(steps)