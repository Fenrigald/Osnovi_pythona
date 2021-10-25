import re


def email_parse(email):
    res = re.findall(r"([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$", email)
    if res:
        return dict(zip(['username','domain'], list(res[0])))
    raise ValueError(f'wrong email: {email}')


if __name__ == '__main__':
    print(email_parse('host@mail.ru'))
    print(email_parse('gostmailru'))
    print(email_parse('front@mailmailcom'))