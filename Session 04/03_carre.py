### Code to complete [START] ###


def carre(n):
    matrix = []
    count = 0
    for l in range(n):
        row = []
        for i in range(n):
            row.append((count)*n + i)
        matrix.append(row)
        count += 1
    return matrix