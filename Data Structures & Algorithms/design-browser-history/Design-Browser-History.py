1class Node:
2    def __init__(self, url):
3        self.url = url
4        self.prev = None
5        self.next = None
6
7
8class BrowserHistory:
9    def __init__(self, homepage: str):
10        self.curr = Node(homepage)
11
12    def visit(self, url: str) -> None:
13        node = Node(url)
14        self.curr.next = node
15        node.prev = self.curr
16        self.curr = node
17
18    def back(self, steps: int) -> str:
19        while steps and self.curr.prev:
20            steps -= 1
21            self.curr = self.curr.prev
22        return self.curr.url
23
24    def forward(self, steps: int) -> str:
25        while steps and self.curr.next:
26            steps -= 1
27            self.curr = self.curr.next
28        return self.curr.url
29
30
31# Your BrowserHistory object will be instantiated and called as such:
32# obj = BrowserHistory(homepage)
33# obj.visit(url)
34# param_2 = obj.back(steps)
35# param_3 = obj.forward(steps)