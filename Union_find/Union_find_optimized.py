# find root with path compression
def find(x, parent):
    if parent[x] != x:
        # update parent to point directly to the root
        parent[x] = find(parent[x], parent)
    return parent[x]

# merge two sets by rank
def union(x,y, parent, rank):
    rootx = find(x, parent)
    rooty = find(y, parent)
    
    # the roots are the same
    if rootx == rooty:
        return
    
    # check rank
    rankx = rank[rootx]
    ranky = rank[rooty]

    # if their ranks are the same -> merge them and update rank
    if rankx == ranky:
        parent[rootx] = rooty
        rank[rooty] += 1
    # if rankx is greater than ranky -> merge y into x
    elif rankx > ranky:
        parent[rooty] = rootx
    # if ranky is greater than rankx -> merge x into y
    else:
        parent[rootx] = rooty

# initialize parent array and rank
def make_set(v):
    parent = [0] * (v)
    rank = [0] * (v)
    for i in range(0, v):
        parent[i] = i
        rank[i] = 0
    return parent, rank

if __name__ == "__main__":
    students = 10
    clues = [[1, 2], [3, 4], [5, 2], [4, 6], [2, 6], [8, 7], [9, 7], [1, 6], [2, 4]]
    leads = len(clues)

    # initialize disjoint sets
    parent, rank = make_set(students)
    for i in range(leads):
        union(clues[i][0], clues[i][1], parent, rank)

    # output the groups 
    groups = {}

    for j in range(1, students):
        root = find(j, parent)
        if root not in groups:
            groups[root] = []
        groups[root].append(j)

    for root, members in groups.items():
        print("Group rooted at", root, ":", members)