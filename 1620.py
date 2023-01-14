if __name__ == "__main__":
    n, m = map(int, input().split())
    numbering = dict()
    pocketmons = [0]
    for i in range(1, n + 1):
        pocket = input()
        numbering[pocket] = i
        pocketmons.append(pocket)

    for _ in range(m):
        temp = input()
        if temp.isdigit():
            print(pocketmons[int(temp)])
        else:
            print(numbering[temp])
