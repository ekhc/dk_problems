import re

def check_ip(text):
    ip_regex = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    try:
        re.search(ip_regex, text).group(0)
        print('YES')
    except AttributeError as e:
        print('NO')

if __name__ == '__main__':
    print('Input:')
    check = input()
    print('Output:')
    check_ip(check)
