# module 2: test Class


class TestDescendantTree:
    def test_type(self):
        assert type(1) == int

    def test_strings(self):
        assert str.upper("python") == "PYTHON"
        assert "pytest".capitalize() == "Pytest"
