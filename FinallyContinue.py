def new_continue():
    for i in range(12):
        try:
            print(i/0)
        except:
            print(i)
        finally:
            print("no error in continue")
            continue

new_continue()
