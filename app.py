class NotePad():
    def __init__(self, note):
        self.notes = [note]
    def open(self):
        pass
    def close(self):
        pass
    def select(self, note_name):
        pass

class Note():
    def __init__(self, content):
        self.content = ""
    def save(self):
        pass
    def save_as(self):
        pass

if __name__ == "__main__":
    print("Starting notepad...")
