"""tests/test_main.py"""
from src.main import add

def test_add():
    """add関数のテスト"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_main_function(capsys):
    """main関数のテスト（標準出力の検証）"""
    from src.main import main
    main()
    captured = capsys.readouterr()
    assert "1 + 2 = 3" in captured.out
