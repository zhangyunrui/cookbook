def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')


def factorial(items):
    head, *tail = items
    return head * factorial(tail) if tail else head


items = range(1, 5)

print(factorial(items))
