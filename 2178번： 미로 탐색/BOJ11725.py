import sys
# this reminds me the find function

# what was the find?
def find(x):
	if parent[x] != x:
		parent[x] = find(x)
	return parent[x]

from collections import deque

def bfs(root: int):
	que = deque()
	que.appendleft(root)
	visited = [False for _ in range(n+1)]
	while que:
		v = que.pop()
		for u in v:
			if not visited[u]:
				visited[u] = True
				parent[u] = v
				print(f'parent[{u}]={v}')
				print(parent)
				# then what? appendleft to que
				que.appendleft(E[u])
	

if __name__ == '__main__':
	input = sys.stdin.readline
	n = int(input().strip())
	arr = [
			tuple(map(int, input().split()))
			for _ in range(n-1)
		]
	
	E = {
		i:[] for i in range(n+1)
	}
	
	for v, u in arr:
		# 간선 그래프 생성
		E[v].append(u)
		E[u].append(v)
	print(E)
	parent = [i for i in range(n+1)]
	bfs(E[1])
	for p in parent:
		print(p)
