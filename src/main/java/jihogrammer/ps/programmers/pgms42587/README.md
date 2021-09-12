# 프린터

>   https://jihogrammer.tistory.com/65

## 프로그래머스

### 성능

| TC        | Python3 Radix  | Java Radix     | Java Queue     |
| --------- | -------------- | -------------- | -------------- |
| 테스트 1  | 0.02ms, 10.4MB | 0.10ms, 72.8MB | 0.81ms, 74.6MB |
| 테스트 2  | 0.04ms, 10MB   | 0.52ms, 72.5MB | 0.88ms, 63.4MB |
| 테스트 3  | 0.01ms, 10.2MB | 0.08ms, 57.6MB | 0.57ms, 60.1MB |
| 테스트 4  | 0.01ms, 10MB   | 0.08ms, 58.3MB | 0.86ms, 68.8MB |
| 테스트 5  | 0.01ms, 10.2MB | 0.09ms, 74.2MB | 0.48ms, 71.3MB |
| 테스트 6  | 0.02ms, 10.2MB | 0.20ms, 72.2MB | 0.58ms, 59.4MB |
| 테스트 7  | 0.01ms, 10.2MB | 0.20ms, 74.4MB | 0.62ms, 71MB   |
| 테스트 8  | 0.02ms, 10.1MB | 0.30ms, 70.1MB | 0.84ms, 61.3MB |
| 테스트 9  | 0.01ms, 10.2MB | 0.12ms, 61.7MB | 0.59ms, 72.5MB |
| 테스트 10 | 0.02ms, 10.1MB | 0.16ms, 74.4MB | 0.58ms, 70.3MB |
| 테스트 11 | 0.02ms, 10.2MB | 0.23ms, 72.8MB | 0.86ms, 59.9MB |
| 테스트 12 | 0.01ms, 10.2MB | 0.06ms, 58.6MB | 0.46ms, 59.4MB |
| 테스트 13 | 0.02ms, 10.2MB | 0.23ms, 70.9MB | 0.86ms, 59.4MB |
| 테스트 14 | 0.01ms, 10.3MB | 0.06ms, 69.2MB | 0.63ms, 69.5MB |
| 테스트 15 | 0.01ms, 10.2MB | 0.05ms, 59.8MB | 0.44ms, 72.2MB |
| 테스트 16 | 0.01ms, 10.2MB | 0.23ms, 70.5MB | 0.63ms, 74.6MB |
| 테스트 17 | 0.02ms, 10.3MB | 0.17ms, 57.6MB | 1.12ms, 71.7MB |
| 테스트 18 | 0.01ms, 10.1MB | 0.22ms, 71MB   | 0.54ms, 71.3MB |
| 테스트 19 | 0.02ms, 10.2MB | 0.19ms, 77.6MB | 0.66ms, 60.8MB |
| 테스트 20 | 0.01ms, 10.1MB | 0.08ms, 59.4MB | 0.61ms, 70.9MB |

### 접근

어리석게도 `스택/큐` 문제라고 명시되어 있어도 그렇게 풀고 싶지 않았다.
큐로 풀 때, 입력이 `[1, 2, 3, 4, 5, 6, 7, 8, 9]` 순으로 주어진다면
쉽게 최악의 경우를 생각할 수 있다.

다른 시선으로 보고 싶어 생각한 방법이 `기수정렬 Radix Sort`이었다.
`기수정렬` 또한 Queue를 사용하는 방식이긴 하다.
어차피 처음에 주어지는 버퍼는 순차적으로 읽어야 한다.
그렇다면 그때부터 구분짓고 문제를 해결하고 싶었다.

엄밀히 말하자면 `기수정렬`로 푸는 방식은 아니다.
`기수정렬`에서 사용하는 방식을 차용했다.
우선순위는 1부터 9까지 9개 종류가 있고, 수가 클수록 우선순위가 높다.
따라서 9개의 바구니(`bucket`, `queue`)를 준비하고,
`priorities`를 순차적으로 각 우선순위에 해당하는 `bucket`에 담는다.
이때 담는 `priority`의 원소가 아닌 `index`값을 `bucket`에 담는다.
그렇게 담게 되면 자연스럽게 각 `bucket` 내부에는 오름차순으로 담긴다.

구분짓는 것은 끝났지만, 이제 문제를 어떻게 해결하는지 생각이 필요하다.
다음의 예로 설명한다.

```py
priority = [1, 3, 3, 2, 4, 5, 3, 2, 4, 5]
```

위처럼 입력이 주어진다고 했을 때 각 바구니에 담으면 다음과 같다.
>   우선순위를 편의상 반대로 넣었다.
>   우선순위 9가 0번 바구니, 8이 1번 바구니 순으로 담았다.

```py
# 바구니 세트
buckets = [[] for _ in range(9)]

# 바구니에 priorities 담기
# 우선순위 조정하고 인덱스 값을 하나씩 담는다.
for i, p in enumerate(priorities):
    buckets[9 - i].append(i)

# 각 바구니에 인덱스 값이 담긴 상태
bucket[0] = []
bucket[1] = []
bucket[2] = []
bucket[3] = []
bucket[4] = [5, 9]
bucket[5] = [4, 8]
bucket[6] = [1, 2, 6]
bucket[7] = [3, 7]
bucket[8] = [0]
```

이렇게 잘 담았다고 가정하고 일단 프린터가 출력되는 순서는 다음과 같다.

```py
# index
[5, 9, 4, 8, 1, 2, 6, 7, 3, 0]
```

조금 더 구분해서 보자.

```py
[5, 9]
[4, 8]
[1, 2, 6]
[7, 3]*
[0]
```

이렇게 보면 `기수정렬`의 의미가 조금 명확해졌다.
하지만 별표 표시한 우선순위를 보면 조금 다른 것을 확인할 수 있다.
`bucket`에 담은 순서와 다른 것을 볼 수 있다.

예외처리라고 하기에는 조금 그렇지만,
쉽게 말하면 **이전 바구니의 마지막 인덱스의 값을 기준으로** 생각해야 한다.
설명을 어떻게 적어야 하는지 모르겠으니까 그림을 마저 그린다.
`[5, 9]`는 이전 바구니가 없으니까 넘어가고 `[4, 8]`부터 본다.

```py
previous_bucket = [5, 9] # 이전 바구니
current_bucket = [4, 8]  # 현재 바구니
```

`이전 바구니`의 마지막 원소의 값은 `9`이다.
`9`보다 큰 원소가 `현재 바구니`에 있다면, 그 원소부터 출력되어야 한다.
만약 `현재 바구니`가 `[4, 8, 10, 11]`이라면,
프린터에서 출력되는 순서는 `[10, 11, 4, 8]` 순이다.

단순히 생각하면 `9`보다 작은 원소는 바구니(Queue)의 맨 뒤로 보내면 된다.
예를 들면 다음과 같이 처리할 수 있다.

```py
pivot = previous_bucket[-1]

# 복사를 하지 않으면 for문에서 고장난다.
# 뒤에서는 아예 다른 방식으로 풀기 때문에 자세한 설명은 생략한다.
temp_bucket = current_bucket.copy()

for b in temp_bucket:
    if b < pivot: current_bucket.append(current_bucket.pop(0))
    else: break
```

하지만 나는 위와 같은 코드가 싫은 것이다.
저렇게 할 거였으면 그냥 Queue로만 풀는 게 더 깔끔하다.

내가 찾은 대안은 이진탐색(BS, UB, LB) 중 하나인 `Upper Bound`이다.
우아하게 풀기 위해서 `upper_bound()`로 `pivot`을 찾아서
바구니를 slice 해서 이어붙인다.

```py
key = previous_bucket[-1]
pivot = upper_bound(key, current_bucket, 0, len(current_bucket))
current_bucket = current_bucket[pivot:] + current_bucket[:pivot]
```

`Upper Bound`에 대한 설명은 링크를 참고하자.

`location`이 출력되는 순서(정답)와 이전 바구니를 결정하는 방법은
코드로 대체하고 넘어간다.

#### Full Code (python)

```py
def upper_bound(key, list, l, r):
    while l < r:
        m = l + r >> 1
        if list[m] > key: r = m
        else: l = m + 1
    return r

def solution(priorities, location):
    buckets = [[] for _ in range(9)]
    prev_bucket = []
    answer = 1

    # 바구니에 우선순위별로 원소(인덱스) 담기
    for i, p in enumerate(priorities):
        buckets[9 - p].append(i)

    # 이전 바구니 결정 및 가지치기
    for i, bucket in enumerate(buckets):
        if not bucket: continue
        if location in bucket:
            return bucket.index(location) + 1
        prev_bucket = buckets.pop(i)
        break

    answer += len(prev_bucket)

    # 우선순위 높은 바구니부터 순차 탐색
    for bucket in buckets:
        if not bucket: continue

        key = prev_bucket[-1]
        pivot = upper_bound(key, bucket, 0, len(bucket))
        prev_bucket = bucket[pivot:] + bucket[:pivot]

        if location in prev_bucket:
            answer += prev_bucket.index(location)
            break

        answer += len(bucket)

    return answer
```
