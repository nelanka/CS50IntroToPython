# https://cs50.harvard.edu/python/2022/psets/1/deep/

answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower()
match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")