

def climbingLeaderboard(scores, alice):

    if not (len(scores) > 0 and len(alice) > 0):
        return []

    scoreIndex = []

    previous = scores[0]
    scoreIndex.append(previous)
    tracker = 1
    counter = len(scores)
    for i in range(1, counter):
        elem = scores[i]

        if elem == previous:
            continue

        previous = scores[i]
        scoreIndex.append(previous)
        tracker = tracker + 1

    rank = len(scoreIndex)
    tracker = len(scoreIndex)-1
    aliceRanks = []
    j = 0
    counter = len(alice)
    for i in range(0, counter):
        for j in range(tracker, -1, -1):
            if alice[i] >= scoreIndex[j]:
                rank = rank - 1
                continue
            break
        tracker = rank - 1
        aliceRanks.append(rank + 1)

    return aliceRanks

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],[120 ,120 ,120 ,120]))
#print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],[5, 25, 50, 120]))
