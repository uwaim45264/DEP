import customtkinter as ctk
import requests
from bs4 import BeautifulSoup
import csv
from tkinter import messagebox, filedialog


# Function to perform web scraping and save data to CSV
def scrape_and_save():
    url = url_entry.get()
    css_selector = selector_entry.get()

    # Make HTTP request to the URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching URL: {e}")
        return

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.select(css_selector)

    # Extract text from the elements
    data = [element.get_text(strip=True) for element in elements]

    # Ask user where to save the CSV file
    csv_filename = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

    if not csv_filename:
        return  # If the user cancels, exit the function

    # Save data to CSV file
    try:
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for item in data:
                writer.writerow([item])
        messagebox.showinfo("Success", f"Data saved to {csv_filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving to CSV: {e}")


# Create main window
root = ctk.CTk()
root.title("Web Scraper")

# Create and place labels and entry widgets for URL and CSS selector
url_label = ctk.CTkLabel(master=root, text="URL:", font=("Arial", 25))
url_label.place(relx=0.1, rely=0.4, anchor="center")
url_entry = ctk.CTkEntry(master=root, width=700, height=50, corner_radius=32, font=("Arial", 20), border_width=3, border_color="#FFFFFF")
url_entry.place(relx=0.5, rely=0.4, anchor="center")

# lable for title web scraper
lable = ctk.CTkLabel(master=root, text="WEB SCRAPER", font=("Arial", 80))
lable.place(relx=0.5, rely=0.1, anchor="center")

# lable for CSS SELECTOR
selector_label = ctk.CTkLabel(master=root, text="CSS SELECTOR:", font=("Arial", 25))
selector_label.place(relx=0.1, rely=0.6, anchor="center")
# entry for CSS SELECTOR
selector_entry = ctk.CTkEntry(master=root, width=700, height=50, corner_radius=32, font=("Arial", 20), border_width=3,
                              border_color="#FFFFFF")
selector_entry.place(relx=0.5, rely=0.6, anchor="center")

# button for save CSS SELECTOR file in user computer
scrape_button = ctk.CTkButton(master=root, text="Save as", command=scrape_and_save, width=300, height=50,
                              corner_radius=32, font=("Arial", 30), border_width=3, border_color="#FFFFFF",
                              fg_color="#008000", hover_color="#228B22")
scrape_button.place(relx=0.5, rely=0.77, anchor="center")

root.geometry("1366x768")
root.mainloop()
