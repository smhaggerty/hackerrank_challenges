def fun(s):
    import re
    filtered_email = re.fullmatch('[\w-]+@[A-Za-z0-9]+[.]\w{0,3}', s)
    return filtered_email

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
