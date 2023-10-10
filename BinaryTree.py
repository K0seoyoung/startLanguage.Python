def preorder(v):
		count = 0
		if v != 0:
			count += 1
			if left[v] != 0:
				count += preorder(left[v])
			if right[v] != 0:
				count += preorder(right[v])
		return count
	
def postorder(v):
		count = 0
		if v != 0:
			if left[v] != 0:
				count += postorder(left[v])
			if right[v] != 0:
				count += postorder(right[v])
			count += 1
		return count

def depth(v):
		depth_ = 0
		while parent[v] != 0:
			v = parent[v]
			depth_ += 1
		return depth_

def is_ancestor(u, v):
		while parent[v] != 0:
			if parent[v] == u:
				return True
			else: 
				v = parent[v]
		return False

def lca(u, v):
	if is_ancestor(u, v):
		return u
	elif is_ancestor(v, u):
		return v
	else:
		sub = depth(u) - depth(v)
		if sub > 0:
			for i in range(sub):
				u = parent[u]
		else:
			for j in range(-sub):
				v = parent[v]

		for k in range(depth(u)):
			if parent[u] == parent[v]:
				return parent[u]
			else:
				u = parent[u]
				v = parent[v]
		return None
# 입력 처리 부분 (여기에)
n = int(input())
parent, left, right = [0]*(n+1), [0]*(n+1), [0]*(n+1)
for i in range(n):
	node = input().split()
	key = int(node[0])
	left_key = int(node[1])
	right_key = int(node[2])
# 전처리 코드 부분 (여기에)
	parent[left_key] = key
	left[key] = left_key
	parent[right_key] = key
	right[key] = right_key
   

#
# 명령 처리 부분으로 아래는 수정 하지 말 것!
#
while True:
		cmd = input().split()
		if cmd[0] == 'exit':
			break
		elif cmd[0] == 'preorder':
			res = preorder(int(cmd[1]))
			print(f"  > preorder({int(cmd[1])}) = {res}")
		elif cmd[0] == 'postorder':
			res = postorder(int(cmd[1]))
			print(f"  > postorder({int(cmd[1])}) = {res}")
		elif cmd[0] == 'depth':
			res = depth(int(cmd[1]))
			print(f"  > depth({int(cmd[1])}) = {res}")
		elif cmd[0] == 'is_ancestor':
			res = is_ancestor(int(cmd[1]), int(cmd[2]))
			print(f"  > {int(cmd[1])} is {'an' if res else 'not an'} ancestor of {int(cmd[2])}")
		elif cmd[0] == 'lca':
			res = lca(int(cmd[1]), int(cmd[2]))
			print(f"  > lca({int(cmd[1])}, {int(cmd[2])}) = {res}")
		else:
			print("illegal command")