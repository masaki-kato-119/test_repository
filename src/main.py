"""src/main.py"""
def add(a: int, b: int) -> int:
    """2つの整数を加算して返すサンプル関数"""
    return a + b

def main():
    """メイン関数"""
    total = add(1,2)
    print(f"1 + 2 = {total}")

if __name__ == "__main__":
    main()
