from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
# import configparser
import json

FP = "moods.json"


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
		self.load_moods()
	
	def load_moods(self):
		with open(FP) as file:
			moods = json.load(file)
			i = 0
			for m in moods['moods']:
				print(i)
				mbtn = MoodButton(self.moods, id=i)
				mbtn.configure(command=mbtn.open)
				i += 1
	def newmood(self):
		addMood = AddMoods()
	
class MoodButton(Button):
	def __init__(self, *args) -> None:

		super().__init__(args)
		if id != None:
			self.id = id
	
	def open(self):
		moodWindow = MoodWindow(id)

class MoodWindow(Tk):
	def __init__(self, id):
		super().__init__()
		self.title(f"Viewing Mood {id}")
		
		with open(FP) as js:
			mood = Mood.from_json(json.load(js)['moods'][id])

		self.text = Label(self, mood.text)

class AddMoods(Tk):
	def __init__(self):
		super().__init__()
		self.title("Expressional Analysis")
		
		self.choice = StringVar(self)
		self.label_user = Label(self, text =f"Thank you for your input, {greetings.ent.get()}.")
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
		

		# print(self.happy_radiobutton)
		# self.insert_centered()
		#user input again
	
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

"""class AddMood(Tk):
	def __init__(self):
		super().__init__()
		self.title("Expressional Analysis")
		
		self.choice = StringVar(self)
		self.label_user = Label(self, text =f"Thank you for your input, {greetings.ent.get()}.")
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
		

		# print(self.happy_radiobutton)
		# self.insert_centered()
		#user input again
	
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

		global tracker 
		tracker = Tracker()
		self.destroy()
"""

class Greeting(Tk):
	def __init__(self) -> None:
		super().__init__()
		self.title("Anonymous Mood Journal")
		self.geometry("700x350")
		self.label = Label(self, text ="Tell me, what is your name?")
		self.label.pack(pady = 10)
		#user input 
		self.ent = Entry(self, text =" ")
		self.ent.pack(pady = 10)
		btn = Button(self, text ="Click to proceed.", command = self.proceed)
		#ent.bind('<Return>', openNewWindow)
		btn.pack(pady = 10) 

	def proceed(self):
		if self.ent.get():
			if len(self.ent.get()) in range(2,32):
				openNewWindow()




greetings = Greeting()


if __name__ == "__main__":
	mainloop()