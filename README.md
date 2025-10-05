# ⏰ Python Digital Clock (Tkinter)

This is a simple digital clock application built using **Python** and the built-in **Tkinter** library. This project was a great introduction to **GUI development** and dynamic updates in Python.

## 💻 Technology Used

* **Language:** Python
* **GUI Library:** Tkinter
* **Modules:** `time`

## ✨ Key Features

* Displays real-time current time (HH:MM:SS PM/AM format).
* Displays the current date (Weekday, Day Month Year).
* Uses the `after()` method to ensure the time updates every second.
* Custom styling with a purple background and bold yellow text.

## ▶️ How to Run Locally

1.  Ensure you have Python (3.x) installed on your system.
2.  Clone or download the `03.py` file.
3.  Open your terminal or command prompt in the project directory and run:
    ```bash
    python 03.py
    ```

## 🧠 What I Learned

This project helped me understand:

* How to set up a basic Tkinter window (`root = tk.Tk()`).
* Formatting date and time strings using **`time.strftime()`**.
* The crucial role of the **`label.after(1000, function)`** method for scheduling recurring tasks and updating the UI in real-time.
