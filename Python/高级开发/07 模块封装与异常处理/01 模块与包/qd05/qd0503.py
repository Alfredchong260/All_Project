
from . import username, password


def check_login(u_name, pwd):
    if u_name == username and pwd == password:
        return True
    return False
