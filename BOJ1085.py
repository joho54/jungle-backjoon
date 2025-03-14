x, y, w, h = tuple(map(int, input().split()))

def get_distances(x, y, w, h):
    # return four distances to the edge
    return [x, w-x, y, h-y]

arr = get_distances(x, y, w, h)
print(min(arr))