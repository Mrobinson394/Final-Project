import tkinter as tk  # Import the tkinter library for GUI
from tkinter import messagebox  # Import messagebox module for displaying messages
from PIL import Image, ImageTk  # Import Image and ImageTk modules from PIL library for image handling
import os  # Import the os module for operating system dependent functionality

class RevolvingImages:
    """Class for managing revolving images display."""

    def __init__(self, master, image_folder):
        """Initialize the RevolvingImages class."""

        self.master = master  # Reference to the Tkinter master window
        self.image_folder = image_folder  # Path to the folder containing images
        self.image_files = ["bird.jpg", "horse.jpg", "bunny.jpg", "cats.jpg", "dog.jpg"]  # List of image filenames
        self.current_index = 0  # Index of the current displayed image
        self.image_label = tk.Label(master)  # Label widget to display images
        self.image_label.pack(side=tk.LEFT, padx=10)  # Pack the label widget to the left with padding
        self.load_image()  # Load the first image

    def load_image(self):
        """Load and display images in a revolving manner."""

        # Construct the path to the current image
        image_path = os.path.join(self.image_folder, self.image_files[self.current_index])

        # Open and resize the image
        image = Image.open(image_path)
        image = image.resize((100, 100))  # Resize the image to fit

        # Convert the image to Tkinter format
        self.photo = ImageTk.PhotoImage(image)

        # Configure the image label to display the current image
        self.image_label.configure(image=self.photo)

        # Update the current index for the next image
        self.current_index = (self.current_index + 1) % len(self.image_files)

        # Schedule the next image load after 2 seconds
        self.master.after(2000, self.load_image)

class PetBoards:
    """Class for managing pet boards."""

    def __init__(self, master):
        """Initialize the PetBoards class."""

        self.master = master  # Reference to the Tkinter master window
        self.master.title("Pet Boards")  # Set the window title
        self.master.geometry("800x400")  # Set the window size

        self.create_widgets()  # Create GUI widgets

    def create_widgets(self):
        """Create GUI widgets for the PetBoards class."""

        # Create and pack GUI widgets
        self.label_title = tk.Label(self.master, text="Welcome to Pet Boards!", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        self.label_info = tk.Label(self.master, text="Explore and create boards to organize your pet-related content.")
        self.label_info.pack()

        self.btn_create_board = tk.Button(self.master, text="Create Board", command=self.create_board)
        self.btn_create_board.pack()

        self.btn_view_boards = tk.Button(self.master, text="View Boards", command=self.view_boards)
        self.btn_view_boards.pack()

        self.btn_exit = tk.Button(self.master, text="Exit", command=self.exit)
        self.btn_exit.pack()

    def create_board(self):
        """Function to handle board creation."""

        messagebox.showinfo("Create Board", "Board creation feature will be implemented later.")

    def view_boards(self):
        """Function to handle board viewing."""

        messagebox.showinfo("View Boards", "Board viewing feature will be implemented later.")

    def exit(self):
        """Function to exit the application."""

        self.master.quit()

class PetHelpApp:
    """Class for managing the main PetHelp application."""

    def __init__(self, master):
        """Initialize the PetHelpApp class."""

        self.master = master  # Reference to the Tkinter master window
        self.master.title("PetHelp")  # Set the window title
        self.master.geometry("800x400")  # Set the window size

        self.create_widgets()  # Create GUI widgets

    def create_widgets(self):
        """Create GUI widgets for the PetHelpApp class."""

        # Create and pack GUI widgets
        self.revolving_images = RevolvingImages(self.master, "images")

        self.label_welcome = tk.Label(self.master, text="Welcome to PetHelp!", font=("Helvetica", 16))
        self.label_welcome.pack(pady=10)

        self.btn_login = tk.Button(self.master, text="Log In", command=self.login)
        self.btn_login.pack()

        self.btn_signup = tk.Button(self.master, text="Sign Up", command=self.signup)
        self.btn_signup.pack()

        self.btn_pet_boards = tk.Button(self.master, text="Pet Boards", command=self.open_pet_boards)
        self.btn_pet_boards.pack()

        self.btn_exit = tk.Button(self.master, text="Exit", command=self.exit)
        self.btn_exit.pack()

    def login(self):
        """Function to handle user login."""

        messagebox.showinfo("Login", "Login functionality will be implemented later.")

    def signup(self):
        """Function to handle user signup."""

        messagebox.showinfo("Sign Up", "Sign Up functionality will be implemented later.")

    def open_pet_boards(self):
        """Function to open the Pet Boards section."""

        root = tk.Toplevel(self.master)  # Create a new top-level window
        app = PetBoards(root)  # Instantiate the PetBoards class in the new window

    def exit(self):
        """Function to exit the application."""

        self.master.quit()

def main():
    """Main function to initialize and run the application."""

    root = tk.Tk()  # Create the Tkinter root window
    app = PetHelpApp(root)  # Instantiate the PetHelpApp class
    root.mainloop()  # Run the Tkinter event loop

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly
