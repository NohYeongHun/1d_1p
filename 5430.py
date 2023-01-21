import sys


class Deque:
    rear = 0
    front = 0
    front_status = True
    MAX_SIZE = 100
    deq = list()

    def __init__(self, arr):
        self.front = 0
        self.MAX_SIZE = len(arr)
        self.rear = len(arr) - 1
        self.deq = [item for item in arr]

    def is_empty(self):
        if self.front_status:
            if self.front > self.rear:
                return True
            else:
                return False
        else:
            if self.rear < self.front:
                return True
            else:
                return False

    def popleft(self):

        if self.is_empty():
            return False
        else:
            front_status = self.front_status
            if front_status:
                temp = self.deq[self.front]
                self.deq[self.front] = 0
                self.front += 1
            else:
                temp = self.deq[self.rear]
                self.deq[self.rear] = 0
                self.rear -= 1
            return temp

    def reverse(self):
        self.front_status = not self.front_status

    def deq_print(self):
        temp = self.deq[self.front:self.rear + 1]
        if not self.front_status:
            temp = temp[::-1]
        print(str(temp).replace(" ", ""))


def input():
    return sys.stdin.readline().rstrip()


def _split(arr):
    return arr.split(",")


def solve(arr, op):
    q = Deque(arr)

    for cmd in op:
        if cmd == 'R':
            q.reverse()
        elif q.is_empty():
            print("error")
            return
        else:
            q.popleft()
    q.deq_print()
    return


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        op = input()
        n = int(input())
        arr = input().replace("[", "").replace("]", "")
        if arr:
            arr = list(map(int, _split(arr)))
        else:
            arr = []
        solve(arr, op)
