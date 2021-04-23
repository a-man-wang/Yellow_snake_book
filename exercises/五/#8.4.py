"""

练习8-4：大号T恤 修改函数make_shirt()，使其在默认情况下制作一件印有“Ilove Python”字样的大号T恤。调用这个函数来制作：一件印有默认字样的大号T恤，
一件印有默认字样的中号T恤，以及一件印有其他字样的T恤（尺码无关紧要）。

"""

def make_shirt(size="大号",slogan="Ilove Python"):
    print(f"尺寸为{size},印刷着{slogan}")

make_shirt()
make_shirt(size="中号")
make_shirt(slogan="其他字样")