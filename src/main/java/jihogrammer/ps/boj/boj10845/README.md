# 큐

## BOJ

### 성능

| Memory   | Time  | Length |
| -------- | ----- | ------ |
| 29452 KB | 76 ms | 487 B  |

### 접근

python이나 JS의 경우 변수에 쉽게 메소드를 할당할 수 있다.

```py
import sys
read = sys.stdin.read
```

위와 같이 변수에 메소드를 할당한다.
C/C++에서도 `define` 등을 통해 간단하게 메소드를 만들 수 있다.
하지만 Java는 불가능하다. 불가능한 건 아니지만, 간편함은 확실히 없다.

이게 접근 방법이다.
python dictionary에 메소드를 아예 매핑했다.
key는 "push", "pop" 등으로 하고,
각 value는 람다식이나 메소드를 매핑해서 사용했다.

읽고 바고 가져다 사용했다.

```py
from sys import stdin

read = stdin.readline

N = int(read())
queue = []
answer = []
command = {
    "push": queue.append,
    "pop": lambda q: q.pop(0) if q else '-1',
    "size": lambda q: str(len(q)),
    "empty": lambda q: '0' if q else '1',
    "front": lambda q: q[0] if q else '-1',
    "back": lambda q: q[-1] if q else '-1'
}

for _ in range(N):
    o, *v = read().split()
    if o == "push": command[o](v[0])
    else: answer.append(command[o](queue))

print('\n'.join(answer))
```