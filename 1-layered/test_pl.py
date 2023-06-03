import pytest
from bl import BL
from pl import PL

@pytest.fixture
def bl_mock():
    class MockBL:
        def get_data(self):
            return ["Mock Data 1", "Mock Data 2"]
    
    bl = MockBL()
    return bl

def test_display_with_mock_data(bl_mock):
    pl = PL(bl_mock)
    expected_output = "Data: Mock Data 1\nData: Mock Data 2\n"
    output = pl.display_bl()
    assert output == expected_output

def test_display_with_no_data(bl_mock):
    bl_mock.get_data = lambda: False
    pl = PL(bl_mock)
    expected_output = "no data"
    output = pl.display_bl()
    assert output == expected_output
