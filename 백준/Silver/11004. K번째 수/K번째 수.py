import sys

N, K = map( int, sys.stdin.readline().split() )

data_list = list( map( int, sys.stdin.readline().split()))

data_list.sort()

print(data_list[K-1])