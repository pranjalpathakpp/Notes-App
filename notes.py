import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.image = None
        self.audio = None
        self.reminder = None

    def add_image(self, image):
        self.image = image
        print("Image added to the note.")

    def add_audio(self, audio):
        self.audio = audio
        print("Audio added to the note.")

    def set_reminder(self, reminder_date):
        try:
            reminder_date = datetime.datetime.strptime(reminder_date, "%d/%m/%Y").date()
            self.reminder = reminder_date
            print("Reminder set for the note.")
        except ValueError:
            print("Invalid date format. Reminder not set.")

    def display(self):
        print("Note Title:", self.title)
        print("Note Content:", self.content)
        if self.image:
            print("Note Image:", self.image)
        if self.audio:
            print("Note Audio:", self.audio)
        if self.reminder:
            print("Note Reminder:", self.reminder.strftime("%d/%m/%Y"))
        print()


class NotesApp:
    def __init__(self):
        self.notes = []

    def add_note(self):
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        note = Note(title, content)
        self.notes.append(note)
        print("Note added successfully.")

    def add_image_to_note(self):
        note_index = int(input("Enter note index: "))
        if note_index >= 0 and note_index < len(self.notes):
            image = input("Enter image filename: ")
            self.notes[note_index].add_image(image)
        else:
            print("Invalid note index.")

    def add_audio_to_note(self):
        note_index = int(input("Enter note index: "))
        if note_index >= 0 and note_index < len(self.notes):
            audio = input("Enter audio filename: ")
            self.notes[note_index].add_audio(audio)
        else:
            print("Invalid note index.")

    def set_reminder_for_note(self):
        note_index = int(input("Enter note index: "))
        if note_index >= 0 and note_index < len(self.notes):
            reminder_date = input("Enter reminder date (dd/mm/yyyy): ")
            self.notes[note_index].set_reminder(reminder_date)
        else:
            print("Invalid note index.")

    def display_notes(self):
        for note in self.notes:
            note.display()

    def run(self):
        while True:
            print("Notes App Menu:")
            print("1. Add Note")
            print("2. Add Image to Note")
            print("3. Add Audio to Note")
            print("4. Set Reminder for Note")
            print("5. Display Notes")
            print("6. Exit")

            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                self.add_note()
            elif choice == 2:
                self.add_image_to_note()
            elif choice == 3:
                self.add_audio_to_note()
            elif choice == 4:
                self.set_reminder_for_note()
            elif choice == 5:
                self.display_notes()
            elif choice == 6:
                break
            else:
                print("Invalid choice. Please try again.")


app = NotesApp()
app.run()

