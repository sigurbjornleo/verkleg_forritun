class Login:
    def __init__(self):
        self.options = """
        Login
    1 - staff innskráning
    2 - manager innskráning
    e - fara úr forritnu
        """
        
    def draw_option(self):
        print(self.options)
        self.prompt_input()
        
    def promp_input(self):
        while True:
            command = input("innsláttur: ")
            if command == "1":
                pass
            elif command == "2":
                pass
            elif command == "3":
                pass
            elif command =="e":
                return
            else:
                print("vitlaust val, reyndu aftur!")
            