def solution(genres, plays):
    answer = []
    albums = {}
    for i in range(len(genres)):
        if genres[i] in albums.keys():
            albums[genres[i]].append([plays[i],i])
        else:
            albums[genres[i]] = [[plays[i],i]]
    album = {}
    for albums in list(albums.values()):
        album[sum(map(lambda x:x[0],albums))] = sorted(albums,reverse=True)
    while album:
        a = album.pop(max(album.keys()))[:2]
        if len(a) == 2 and a[0][0] != a[1][0]:
            answer += list(map(lambda x:x[1],a))
        else:
            answer += reversed(list(map(lambda x:x[1],a)))
    return answer