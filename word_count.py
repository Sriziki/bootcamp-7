def words(strings):
    a = {}

    for i in strings.split():
        if i.isdigit():
            i = int(i)

        if a.get(i):
            a[i] += 1

        else:
            a[i] = 1

    return a         
