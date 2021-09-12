def upper_bound(key, list, l, r):
    while l < r:
        m = l + r >> 1
        if list[m] > key: r = m
        else: l = m + 1
    return r

def solution(priorities, location):
    buckets = [[] for _ in range(9)]
    before_bucket = []
    answer = 1

    for i, p in enumerate(priorities):
        buckets[9 - p].append(i)

    for i, bucket in enumerate(buckets):
        if not bucket: continue
        if location in bucket:
            return bucket.index(location) + 1
        before_bucket = buckets.pop(i)
        break

    answer += len(before_bucket)

    for bucket in buckets:
        if not bucket: continue

        key = before_bucket[-1]
        pivot = upper_bound(key, bucket, 0, len(bucket))
        bucket = bucket[pivot:] + bucket[:pivot]

        if location in bucket:
            answer += bucket.index(location)
            break

        before_bucket = bucket
        answer += len(bucket)

    return answer
