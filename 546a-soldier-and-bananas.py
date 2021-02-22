k, n, w = map(int, input().split())
borrow = k * w * (w + 1) / 2 - n
print(int(max(borrow, 0)))