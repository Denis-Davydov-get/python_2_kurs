orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


def find_farthest_orbit(list_of_orbits):
    i_max = 0
    s_max = 0
    for i, el_tuple in enumerate(list_of_orbits):
        s_cur = el_tuple[0] * el_tuple[1]
        if el_tuple[0] != el_tuple[1] and s_max < s_cur:
            i_max = i
            s_max = s_cur
    return list_of_orbits[i_max]

print(find_farthest_orbit(orbits))