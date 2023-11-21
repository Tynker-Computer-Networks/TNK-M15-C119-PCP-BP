from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox
import threading
import random


class SecretSanta(Tk):
    def __init__(self):
        super().__init__()
        self.title("Secret Santa App")

        self.frame = Frame()
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        Label(self.frame, text="Participant Name:").grid(
            column=0, row=0, sticky="w")
        self.participant_name_entry = Entry(self.frame)
        self.participant_name_entry.grid(
            column=1, row=0, padx=10, pady=5, columnspan=2)

        Label(self.frame, text="Participant Email:").grid(
            column=0, row=1, sticky="w")
        self.participant_email_entry = Entry(self.frame)
        self.participant_email_entry.grid(
            column=1, row=1, padx=10, pady=5, columnspan=2)

        # Create a Label with the name Participant Wishlist.
        


        # Create a button with the name Add Participant.
      


        Label(self.frame, text="Participants List:").grid(
            column=0, row=4, sticky="w")
        self.participants_listbox = Listbox(self.frame)
        self.participants_listbox.grid(
            column=1, row=4, padx=10, pady=5, columnspan=2)

        Label(self.frame, text="Sender's Email:").grid(
            column=0, row=5, sticky="w")
        self.sender_email_entry = Entry(self.frame)
        self.sender_email_entry.grid(
            column=1, row=5, padx=10, pady=5, columnspan=2)

        Label(self.frame, text="Sender's Password:").grid(
            column=0, row=6, sticky="w")
        self.sender_password_entry = Entry(self.frame, show="*")
        self.sender_password_entry.grid(
            column=1, row=6, padx=10, pady=5, columnspan=2)

        # Create a button with the name Notify Santa and on button press call handle_assignments function.
        

        self.status_label = Label(self.frame, text="", fg="green")
        self.status_label.grid(column=1, row=12, padx=10,
                               pady=10, columnspan=2)

        # Declare the variable isEmailNotSent to check the email is sent or not to the participiants.
        

        # List to keep track of participants
        

    # Function to add the participant to the list.
    def add_participant(self):
        name = self.participant_name_entry.get()
        email = self.participant_email_entry.get()
        wishlist = self.participant_whishlist_entry.get()
        if (name and email and wishlist):
            self.participants.append((name, email, wishlist))
            self.update_listbox()
            self.participant_name_entry.delete(0, END)
            self.participant_email_entry.delete(0, END)
            self.participant_whishlist_entry.delete(0, END)

    # Function to update the listbox
    def update_listbox(self):
        self.participants_listbox.delete(0, END)
        for participant in self.participants:
            self.participants_listbox.insert(END, participant[0])

    # Define handle_assignments() function
    

    # Function to send Secret Santa assignments
    def send_assignments(self):

        if len(self.participants) < 3:
            self.status_label.config(
                text="At least 3 participants are required.")
            return

        random.shuffle(self.participants)

        self.assignments = self.participants.copy()

        while self.has_self_assignments():
            random.shuffle(self.assignments)

        for i, participant in enumerate(self.participants):
            name, email, w = participant
            assigned_to = self.assignments[i][0]
            wishlist = self.assignments[i][2]

            self.send_email(name, email, assigned_to, wishlist)

        # Check if email is sent or not using variable isEmailNotSent.

            # Show the message box after sending the assignment.
            

    # Function to check for self-assignments
    def has_self_assignments(self):
        for i in range(len(self.participants)):
            if self.participants[i][0] == self.assignments[i][0]:
                return True
        return False

    # Function to send email assignments
    def send_email(self, recipient_name, recipient_email, assigned_to, wishlist):
        try:
            sender_email = self.sender_email_entry.get()
            password = self.sender_password_entry.get()

            smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
            smtp_server.starttls()
            smtp_server.login(sender_email, password)

            subject = "Your Secret Santa Assignment"
            msg_body = f"Hello {recipient_name},\n\nYour Secret Santa assignment is: {assigned_to}\n\nWishlist: {wishlist}"

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(msg_body, "plain"))

            smtp_server.sendmail(
                sender_email, recipient_email, message.as_string())
            smtp_server.quit()

        except Exception as e:
            # Replace print with messagebox.showerror() and make the isEmailNotSent to True

            print("Error", f"An error occurred:{str(e)}")


def main():
    app = SecretSanta()
    # Instead of send_email call mainloop() function
    app.send_email()


if __name__ == "__main__":
    main()
