MELODIES = {
        "Katyuscha": [10, 9, 11, 9, 11, 9, 0, 11, 9, 11, 9, 11, 5, 6],
        "Helan går": [3, 9, 3, 7, 0, 8, 8, 3, 7],
        "Studentsången": [9, 11, 9, 9, 0, 11, 11, 9, 9, 9, 2],
        "Åh hur salitg att få vandra": [8, 11, 8, 11, 0, 8, 11, 8, 11, 0, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4],
        "Rule Britannia": [13, 10, 10, 0, 6, 6, 12, 0, 10, 11, 10, 11],
        "Du gamla du fria": [11, 10, 11, 11, 11, 0, 11, 10, 11, 11, 11],
        "Stort block med text": [100]
}

def pick_melody(n):
        return MELODIES[list(MELODIES.keys())[n]]
