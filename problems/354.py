"""
354. 俄罗斯套娃信封问题
"""
import bisect

def maxEnveloples(envelopes):
    if not envelopes:
        return 0
    envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
    n = len(envelopes)
    f = [1] * n
    for i in range(1, n):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                f[i] = max(f[i], f[j] + 1)
    return max(f)

def maxEnvelopes2(envelopes):
    if not envelopes:
        return 0
    envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
    n = len(envelopes)
    f = [envelopes[0][1]]
    for _, h in envelopes[1:]:
        if h > f[-1]:
            f.append(h)
        else:
            index = bisect.bisect_left(f, h)
            f[index] = h
    return len(f)
print(maxEnveloples([[5,4],[6,4],[6,7], [7,5],[2,3]]))
print(maxEnvelopes2([[5,4],[6,4],[6,7], [7,5],[2,3]]))
