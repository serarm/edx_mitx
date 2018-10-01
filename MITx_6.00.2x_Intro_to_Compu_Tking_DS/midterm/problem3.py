def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    result=[]
    songs_copy=songs[0:1:1]+sorted(songs[1:],key=lambda x:x[2])
    l_size=0.0
    # print(songs_copy)
    for i in range(len(songs_copy)):
        l_size=l_size+float(songs_copy[i][2])
        if l_size>max_size:
            return result
        else:
            result.append(songs_copy[i][0])
    return result


assert song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 20)==['a', 'd', 'c', 'b']
assert song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 12.2)==['a', 'd', 'c']
assert song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 11)==['a', 'd']
assert song_playlist([('a', 4.0, 4.4), ('b', 7.7, 3.5), ('c', 6.9, 5.1), ('d', 1.2, 2.7)], 20)==['a', 'd', 'b', 'c']
assert song_playlist([('a', 4.0, 4.4), ('b', 7.7, 3.5), ('c', 6.9, 5.1), ('d', 1.2, 2.7)], 12.3)==['a', 'd', 'b']
assert song_playlist([('a', 1.4, 4.0)], 20)==['a']
print("All testcases pass")

