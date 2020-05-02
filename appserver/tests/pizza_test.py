import pytest
from app.models import Account

@pytest.mark.parametrize('username, email', [
    ('boss', 'boss@corp.com'),
    ('pleb', 'pleb@corp.com'),
])
def test_can_create_account(session, username, email):
    account = Account(username=username, email=email)
    session.add(account)
    session.flush()
    assert account.username == username
    assert account.email == email
