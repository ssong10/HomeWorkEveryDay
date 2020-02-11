dy,dx = [1,-1,0,0],[0,0,-1,1]

for tc in range(int(input())):
    N = int(input())
    atoms = {}
    for _ in range(N):
        x,y,d,k = map(int,input().split())
        atoms[(x*2,y*2)] = [d,k]
    result = 0
    for i in range(4002):
        if not atoms or len(atoms) < 2:
            break
        new_atoms = {}
        dellist = set()
        for (x,y),[d,k] in atoms.items():
            xx,yy = x+dx[d],y+dy[d]
            if (xx,yy) in new_atoms:
                dellist.add((xx,yy))
                new_atoms[(xx,yy)][1] += k
            else:
                new_atoms[(xx,yy)] = [d,k]
        for d in dellist:
            result += new_atoms[d][1]
            del new_atoms[d]
        atoms = new_atoms
    print(f'#{tc+1} {result}')