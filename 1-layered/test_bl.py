import pytest
from bl import BL
from dal import DAL

@pytest.fixture
def dal_conn():
    dal = DAL()
    return dal

def test_get_data_with_empty_db(dal_conn):
    bl = BL(dal_conn)
    data = bl.get_data()
    assert data == False

def test_get_data_with_non_empty_db(dal_conn):
    dal_conn.connect([])
    dal_conn.create("Data 1")
    dal_conn.create("Data 2")
    bl = BL(dal_conn)
    data = bl.get_data()
    assert data == ["Data 1", "Data 2"]