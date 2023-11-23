Secret Santa-2
==================


In this activity, you will learn to create the GUI for the secret santa app.


<img src= "https://media.slid.es/uploads/1525749/images/10933633/PCP.gif" width = "480" height = "320">


Follow the given steps to complete this activity:


1. Create the required widgets.


* Open the file `main.py`.


* Create the widget and place them using the grid geometric manager.
~~~python
        Label(self.frame, text="Participant Wishlist:").grid(column=0, row=2, sticky="w")
        self.participant_whishlist_entry = Entry(self.frame)
        self.participant_whishlist_entry.grid(column=1, row=2, padx=10, pady=5, columnspan=2)




        self.add_button = Button(self.frame, text="Add Participant")
        self.add_button.grid(column=1, row=3, padx=10, pady=5, columnspan=2)


        Label(self.frame, text="Participants List:").grid(column=0, row=4, sticky="w")
        self.participants_listbox = Listbox(self.frame)
        self.participants_listbox.grid(column=1, row=4, padx=10, pady=5, columnspan=2)


        self.send_button = Button(self.frame, text="Notify Santa")
        self.send_button.grid(column=1, row=11, padx=10, pady=10, columnspan=2)


        self.status_label = Label(self.frame, text="", fg="green")
        self.status_label.grid(column=1, row=12, padx=10, pady=10, columnspan=2)
~~~


2. Save the list of the participants.
* Create a list to keep track of the participants.
~~~python
 def __init__(self):
	. . .
self.participants=[]
self.assignments=[]
~~~
* Add the participants to the list.
~~~python
 def __init__(self):
	. . .
	Button(self.frame, text="Add Participant", command=self.add_participant)
~~~
3. Notify the santa.
* Send the mail to the santa with the assigned name.
~~~python
 def __init__(self):
	. . .
Button(self.frame, text="Notify Santa", command=self.handle_assignments)
def save_name():
	. . .
	gameWindow()
~~~
* Save and run the code to check the output.
