import sys
import math
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(math.lcm(a, b))

