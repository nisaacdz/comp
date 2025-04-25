n, m = map(int, input().split())

stargates = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    stargates[a - 1].append((b, c))
    stargates[b - 1].append((a, c))

arrivals = []
for _ in range(n):
    data = list(map(int, input().split()))
    arrivals.append(data[1::])

visited = [False for _ in range(n)]

def traverse(currentPlanet, currentTime):
    if currentPlanet == n:
        return currentTime
    
    for v in arrivals[currentPlanet - 1]:
        if v < currentTime or v > currentTime:
            break
        currentTime += 1

    visited[currentPlanet - 1] = True
    minTime = 100000000
    for (nextPlanet, time) in stargates[currentPlanet - 1]:
        if not visited[nextPlanet - 1]:
            minTime = min(minTime, traverse(nextPlanet, currentTime + time))
    
    return minTime

res = traverse(1, 0)
print(-1 if res == 100000000 else res)