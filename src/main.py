def add(a: int, b: int) -> int:
    """2つの整数を加算して返すサンプル関数"""
    return a + b

def main():
    sum = add(1,2)
    print(f"1 + 2 = {sum}")

if __name__ == "__main__":
    main()