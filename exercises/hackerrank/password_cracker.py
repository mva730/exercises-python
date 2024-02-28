def password_cracker(passwords, login_attempt):
    cont = []
    word = ''
    for i in login_attempt:
        word += i
        if word in passwords:
            cont.append(word)
            word = ''
    if ''.join(cont) != login_attempt:
        return "WRONG PASSWORD"
    return ' '.join(cont)


print(password_cracker('we web adaman barcod'.split(' '), 'webadaman'))
