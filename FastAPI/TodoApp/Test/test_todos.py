import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..database import Base
from ..routers.auth import get_db, get_current_user
from ..main import app
from fastapi.testclient import TestClient
from fastapi import status

#* Load environment variables
load_dotenv()
TESTING_DB_URL = os.getenv('TESTING_DB_URL')

#* Set up in-memory SQLite engine for testing
engine = create_engine(
    TESTING_DB_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

#* Create a session factory bound to the test engine
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#* Create all tables
Base.metadata.create_all(bind=engine)

#* Dependency override for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Dependency override User
def override_get_current_user():
    return {'username': 'ale', 'id': 1, 'user_role': 'admin'}

#* Apply the override
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

def test_read_all_authenticated():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK

