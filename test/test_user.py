import sys
# run pytest in /test
sys.path += ['../src']

from user_input import *

import io

def test_username(monkeypatch):
    username = "myusernae"
    email = "myuser@example.com"
    password = "P@assw0rd"
    monkeypatch.setattr('sys.stdin', io.StringIO(username+"\n"+email+"\n"+password+"\n"))
    username, email, password = get_user_input()
    assert validate_username(username) == True
    assert validate_email(email) == True
    assert validate_password(password) == True