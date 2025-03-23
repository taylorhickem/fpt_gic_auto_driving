

class InteractiveApp:
    def __init__(self, input_fn=input, output_fn=print):
        self.input_fn = input_fn
        self.output_fn = output_fn

    def run(self):
        name = self.input_fn("Enter your name: ")
        self.output_fn(f"Hello, {name}!")
        
        while True:
            answer = self.input_fn("Do you want to continue? (y/n): ")
            if answer.lower() == "n":
                self.output_fn("Goodbye!")
                break
            elif answer.lower() == "y":
                self.output_fn("Great! Let's continue...")
            else:
                self.output_fn("Please enter y or n.")