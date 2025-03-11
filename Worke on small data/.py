class spam:
    def __del__(self):
        print(f"Delete")

x = spam()
x = spam()