test_case = int(input())
for _ in range(test_case):
    n = int(input())
    array = list(map(int, input().split()))
    answer = 10**6 * 5

    for i in range(n):
        for j in range(i + 1, n):
            possible_case = array[i] + array[j] + j - i
            answer = min(answer, possible_case)

    print(answer)