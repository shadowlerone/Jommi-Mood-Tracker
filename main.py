# from tkinter import *
# from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
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
		return mood
	def to_json(self):
		return {
			"emotion": self.emotion,
			"text": self.text
		}

class Tracker(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Moods")
		self.moods = ttk.Frame(self)
		self.new_mood = ttk.Button(self, text="Create entry", command=self.newmood)
		self.new_mood.pack(pady=40)
		self.load_moods()
		self.moods.pack(pady=40)

	def load_moods(self):
		with open(FP) as file:
			moods = json.load(file)
			self.moods_list = [MoodFrame.from_mood(self.moods, Mood.from_json(m)).pack(expand=True, fill=tk.BOTH) for i, m in enumerate(moods['moods'])]
			# [m.pack() for m in self.moods_list]

	def newmood(self):
		addMood = AddMoods(self)
	
class MoodFrame(ttk.Frame):
	def __init__(self, *args) -> None:
		super().__init__(args[0])

	def from_mood(master, mood: Mood):
		m = MoodFrame(master)
		m.emotion = ttk.Label(m, text=mood.emotion)
		m.text = ttk.Label(m, text=mood.text)
		m.emotion.pack(side=tk.LEFT)
		m.text.pack(side=tk.RIGHT)
		return m

class AddMoods(tk.Tk):
	def __init__(self, parent):
		super().__init__()
		self.title("Expressional Analysis")
		self.choice = tk.StringVar(self)
		self.label_user = ttk.Label(self, text =f"Thank you for your input, {name}.")
		self.label_user.grid(row=0, column=0)
		self.empty_spot = ttk.Label(self, text = "Select the emotion that best suits your current mood.")
		self.empty_spot.grid(row=1, column=0)
		self.happy_radiobutton = ttk.Radiobutton(self, text="Happy", variable=self.choice, value="Happy")
		self.happy_radiobutton.grid(row=2, column=0)
		self.sad_radiobutton = ttk.Radiobutton(self, text="Upset", variable=self.choice, value="Upset")
		self.sad_radiobutton.grid(row=3, column=0)
		self.mad_radiobutton = ttk.Radiobutton(self, text="Angry", variable=self.choice, value="Angry")
		self.mad_radiobutton.grid(row=4, column=0)
		self.neutral_radiobutton = ttk.Radiobutton(self, text="Neutral", variable=self.choice, value="Neutral")
		self.neutral_radiobutton.grid(row=5, column=0)
		self.label = ttk.Label(self, text ="Now, what is your forgettable story?")
		self.label.grid(row=6,column=0)
		self.entryy = tk.Text(self, height=10)
		self.entryy.grid(row=7,column=0)
		self.purge = ttk.Button(self, text ="Terminate Session", command = self.terminate)
		self.purge.grid(row=8,column=0)
		self.parent = parent
	
	def terminate(self):
		choice = self.choice.get()
		text = self.entryy.get("1.0", tk.END)
		mood = Mood(text=text.strip(), mood=choice)

		with open(FP) as js:
			moods = json.load(js)
			moods['moods'].append(mood.to_json())
			with open(FP, 'w') as js:
				json.dump(moods, js)
		self.parent.load_moods()
		self.destroy()

class Greeting(tk.Tk):
	def __init__(self) -> None:
		super().__init__()
		self.title("Anonymous Mood Journal")
		self.geometry("700x350")
		self.label = ttk.Label(self, text ="Tell me, what is your name?")
		self.label.pack(pady = 10)
		self.ent = ttk.Entry(self, text =" ")
		self.ent.pack(pady = 10)
		btn = ttk.Button(self, text ="Click to proceed.", command = self.proceed)
		self.error = ttk.Label(self)
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
	tk.mainloop()