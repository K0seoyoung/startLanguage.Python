def solve(A):
	# code here
	many = dict()
	many[0] = -1
	
	count_0 = 0
	count_1 = 0
	result = 0
	for i in range(len(A)):
		if A[i] == '0':
			count_0 += 1
		else:
			count_1 += 1
			
		if many.get(count_1 - count_0) != None:
			result = max(result, i - many[count_1 - count_0])
		else:
			many[count_1 - count_0] = i
	return result
	
A = input().strip()
print(solve(A))
# 사용한 자료구조와 알고리즘을 간략히 설명하고 수행시간을 분석하고 Big-O로 표기
# 해시테이블을 이용한 탐색을 하는 것이 가장 효율적인 방법이라 생각했습니다.
# 따라서 문자열을 탐색하면서 1의 개수와 0의 개수를 각각 count_1,count_0이라 정하고 count했습니다.
# 현재 두 개수 간의 차이를 모아둔 해시테이블을 확인합니다.: 모든 차이를 나타내는 인덱스를 저장합니다
# 저장했던 인덱스와 같은 값을 보유한 인덱스의 차이 중 가장 큰 값을 지정합니다. 이 결과는 최대 길이의 균형 부문자열에 해당합니다.
# O(n)
# for문에 두 번째 if-else문에서 n번 반복하기때문에 O(n)이다. 