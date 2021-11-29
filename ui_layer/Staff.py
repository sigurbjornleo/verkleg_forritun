class Staff:
    def __init__(self):
        self.options = """
        Staff valmynd
    1 - Fasteignir
    2 - Viðgerðir
    3 - Verktakar
    e - fara til baka
        """
     
    def draw_option(self):
        print(self.options)
        self.prompt_input()
        
    def promp_input(self):
        while True:
            command = input("innsláttur: ")
            if command == "1":
                pass
            if command == "2":
                pass
            if command == "3":
                pass
            elif command =="e":
                return "e"
            else:
                print("vitlaust val, reyndu aftur!")
            print(self.options)   
    