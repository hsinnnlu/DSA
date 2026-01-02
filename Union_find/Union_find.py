# find root
def find(x, parent):
    if parent[x] == x:
        return x
    return find(parent[x], parent)

# merge two sets
def union(x,y, parent):
    rootx = find(x, parent)
    rooty = find(y, parent)

    # if the roots are different, merge them
    if rootx != rooty:
        parent[rootx] = rooty

# initialize parent array
def make_set(v):
    parent = [0] * (v)
    for i in range(0, v):
        parent[i] = i
    return parent

if __name__ == "__main__":
    students = 10
    clues = [[1, 2], [3, 4], [5, 2], [4, 6], [2, 6], [8, 7], [9, 7], [1, 6], [2, 4]]
    leads = len(clues)

    # initialize disjoint sets
    parent = make_set(students)
    for i in range(leads):
        union(clues[i][0], clues[i][1], parent)

    # output the groups 
    groups = {}

    for j in range(1, students):
        root = find(j, parent)
        if root not in groups:
            groups[root] = []
        groups[root].append(j)

    for root, members in groups.items():
        print("Group rooted at", root, ":", members)
