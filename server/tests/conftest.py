import pytest
from server.app import create_app
from server.models import db
from server.models import User


@pytest.fixture(scope="module")
def client():

    flask_app = create_app("TestConf")

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            test_user = User(
                username="adele", email="adele.gaudry@gmail.com", password=None
            )
            test_user.set_password("ramen")
            db.session.add(test_user)
            db.session.commit()
            yield testing_client
            db.session.close()
            db.drop_all()
