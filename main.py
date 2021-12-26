from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
# import configparser
import json

FP = "moods.json"
name = ""

def openNewWindow(*arg):
	newWindow = Tracker()
	greetings.destroy()
class Mood():
	def __init__(self, mood = None, text = None):
		if mood:
			self.emotion = mood
		if text:
			self.text = text
	def from_json(json_data):
		mood = Mood()
		mood.emotion = json_data['emotion']
		mood.text = json_data['text']
		return Mood()
	def to_json(self):
		return {
			"emotion": self.emotion,
			"text": self.text
		}

class Tracker(Tk):
	def __init__(self):
		super().__init__()
		self.title("Moods")
		self.moods = Frame(self)
		self.new_mood = Button(self, text="Create entry", command=self.newmood)
		self.new_mood.pack(pady=10)
	def load_moods(self):
		with open(FP) as file:
			moods = json.load(file)
			for i, m in enumerate(moods['moods']):
				mbtn = MoodLabel(self.moods, id=i)

	def newmood(self):
		addMood = AddMoods()
	
class MoodLabel(Label):
	def __init__(self, *args) -> None:
		super().__init__(args)

class AddMoods(Tk):
	def __init__(self):
		super().__init__()
		self.title("Expressional Analysis")
		self.choice = StringVar(self)
		self.label_user = Label(self, text =f"Thank you for your input, {name}.")
		self.label_user.grid(row=0, column=0)
		self.empty_spot = Label(self, text = "Select the emotion that best suits your current mood.")
		self.empty_spot.grid(row=1, column=0)
		self.happy_radiobutton = Radiobutton(self, text="Happy", variable=self.choice, value="Happy")
		self.happy_radiobutton.grid(row=2, column=0)
		self.sad_radiobutton = Radiobutton(self, text="Upset", variable=self.choice, value="Upset")
		self.sad_radiobutton.grid(row=3, column=0)
		self.mad_radiobutton = Radiobutton(self, text="Angry", variable=self.choice, value="Angry")
		self.mad_radiobutton.grid(row=4, column=0)
		self.neutral_radiobutton = Radiobutton(self, text="Neutral", variable=self.choice, value="Neutral")
		self.neutral_radiobutton.grid(row=5, column=0)
		self.label = Label(self, text ="Now, what is your forgettable story?")
		self.label.grid(row=6,column=0)
		self.entryy = Text(self, height=10)
		self.entryy.grid(row=7,column=0)
		self.purge = Button(self, text ="Terminate Session", command = self.terminate)
		self.purge.grid(row=8,column=0)
	
	def terminate(self):
		choice = self.choice.get()
		text = self.entryy.get("1.0", END)
		print(choice)
		print(text)
		mood = Mood(text=text, mood= choice)

		with open(FP) as js:
			moods = json.load(js)
			moods['moods'].append(mood.to_json())
			print(type(moods))
			with open(FP, 'w') as js:
				json.dump(moods, js)
		self.destroy()

class Greeting(Tk):
	def __init__(self) -> None:
		super().__init__()
		self.title("Anonymous Mood Journal")
		self.geometry("700x350")
		self.label = Label(self, text ="Tell me, what is your name?")
		self.label.pack(pady = 10)
		self.ent = Entry(self, text =" ")
		self.ent.pack(pady = 10)
		btn = Button(self, text ="Click to proceed.", command = self.proceed)
		self.error = Label(self)
		self.error.pack()
		btn.pack(pady = 10) 
	def proceed(self):
		if self.ent.get():
			if len(self.ent.get()) in range(2,32):
				global name
				name = self.ent.get()
				openNewWindow()
			else:
				self.error['text'] = "Please enter a name between 2 and 32 characters long."
		else:
			self.error['text'] = "Please enter a name"




greetings = Greeting()


if __name__ == "__main__":
	mainloop()