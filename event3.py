import time

class VirtualTape:
    def __init__(self):
        self.tape = []

    def add_content(self, content):
        self.tape.append(content)

    def cut_tape(self):
        cut_piece = self.tape[:]
        self.tape = []
        return cut_piece

class FarewellTape(VirtualTape):
    def __init__(self, event):
        super().__init__()
        self.event = event

    def farewell_cut(self):
        print(f"The {self.event} AbHINANDANA 2k24...")
        time.sleep(2)
        print("The tape is being cut...")
        time.sleep(2)
        cut_piece = self.cut_tape()
        print("The tape has been cut!")
        time.sleep(1)
        print("Here is the piece:")
        for piece in cut_piece:
            print(piece)
        print("Thank you for being a part of this virtual tape cutting event!")

# Example usage
if __name__ == "__main__":
    farewell_tape = FarewellTape("ABHINANDANA 2k24")
    farewell_tape.add_content("hapiee farewell")
    farewell_tape.add_content("Memories shared")
    farewell_tape.add_content("Well wishes")

    farewell_tape.farewell_cut()
