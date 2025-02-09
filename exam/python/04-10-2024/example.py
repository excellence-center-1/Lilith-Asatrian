
def is_subset(tup1, tup2):
    for item in tup1:
        if item not in tup2:
            return False
    return True

def find_who_likes(tup, dict):
    if tup in dict:
        return dict[tup]
    else:
        possible_matches = []
        for key in dict:
            if is_subset(tup, key):
                possible_matches.append(dict[key])
        if possible_matches:
            min_len_i = possible_matches[0]
            for item in possible_matches:
                if len(item)<len(min_len_i):
                    min_len_i = item
            return min_len_i
    return 'No one'

who_likes = {
    ('kapreze',): ['Lilit', 'Rita', 'Vahan', 'Davit'],
    ('kapreze', 'caesar'): ['Lilit', 'Vahan', 'Davit'],
    ('kapreze', 'bolognese', 'caesar', 'chicken'): ['Davit', 'Lilit'],
    ('caesar',): ['Lilit', 'Vahan', 'Astghik', 'Avnik', 'Davit'],
    ('bolognese', 'khachapuri'): 'Argishti'
}

print(find_who_likes(('kapreze', 'caesar', 'bolognese'), who_likes))
print(find_who_likes(('kapreze',), who_likes))