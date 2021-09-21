import os
import tempfile

import pytest

from app import create_app
from app.dba.db import init_db


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(config_env="testing")

    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_root_front(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert b'Hello, Zakaria MORCHID!' in rv.data