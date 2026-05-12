def count_cows(N, a, b):
    # 결과 저장 배열
    results = [0] * (N + 1)

    # 현재 상태에서 a[i] == b[i]인 경우 체크
    original_matches = [1 if a[i] == b[i] else 0 for i in range(N)]
    original_count = sum(original_matches)

    # 모든 l, r에 대해 검진받는 소의 수 계산
    for l in range(N):
        current_matches = original_count
        for r in range(l, N):
            # 뒤집기: l <= i <= r이면 검진 가능 여부 반전
            if a[r] == b[r]:
                current_matches -= 1
            else:
                current_matches += 1

            # 결과 갱신
            results[current_matches] += 1

    return results

# 입력 예제
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 실행
output = count_cows(N, a, b)
for result in output:
    print(result)
