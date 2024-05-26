class VirtualTape:
    def __init__(self):
        self.tape = []

    def add_content(self, content):
        self.tape.append(content)

    def cut_tape(self):
        cut_piece = self.tape[:]
        self.tape = []
        return cut_piece

# Example usage
if __name__ == "__main__":
    virtual_tape = VirtualTape()
    virtual_tape.add_content("Piece 1")
    virtual_tape.add_content("Piece 2")
    virtual_tape.add_content("Piece 3")

    print("Tape contents before cutting:", virtual_tape.tape)

    cut_piece = virtual_tape.cut_tape()

    print("Cut piece:", cut_piece)
    print("Tape contents after cutting:", virtual_tape.tape)
