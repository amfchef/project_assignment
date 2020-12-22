class Update_to_txt:
    def update_to_txt(self, input):
        f = open("nameday.txt", "w")
        f.write(input)

        f.close()
