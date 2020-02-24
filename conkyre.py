

class SeeFiles:



    def __init__(self, x):
        self.x = x

    def get_whole_file(self):
        with open(self.x, "rt") as my_w_file:
            contents = my_w_file.read()
            print("\n" + contents)

    def get_line_file(self):
        with open(self.x, "rt") as my_l_file:
            for my_line in my_l_file:
                print("\n" + my_line)

    def get_list_file(self):
        my_list = []
        with open(self.x, "rt") as ml:
            for my_l in ml:
                my_list.append(my_l.rstrip('\n'))
        print(my_list)
        print(my_list[0].find("test"))

    def update_file(self):
        f = open(self.x, "a+")
        f.close()


        


























