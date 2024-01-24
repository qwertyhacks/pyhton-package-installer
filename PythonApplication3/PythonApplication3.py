import subprocess
import requests
from tkinter import Tk, StringVar, ttk, Button, Label, Entry, Frame, font, Text

def install_packages(selected_package):
    subprocess.run(['pip', 'install', selected_package])

def on_install_button_click():
    selected_package = package_var.get()
    install_packages(selected_package)

def submit_feedback():
    username = username_entry.get()
    feedback_text = feedback_entry.get("1.0", "end-1c")
    feedback_display.insert("end", f"\nUser: {username}\nFeedback:\n{feedback_text}\n{'='*30}\n")
    send_feedback_to_discord(username, feedback_text)

def send_feedback_to_discord(username, feedback_text):
    webhook_url = 'https://discord.com/api/webhooks/1199543798959710208/7W6rN6pbP3NTOoNTtlYX54XGRfl5Gpiexs1RwVX60hvXIhjMmCtyIPIswLsmvPzE7y3U'
    payload = {'content': f'New Feedback from {username}:\n{feedback_text}'}
    requests.post(webhook_url, json=payload)

# List of available packages
available_packages = [
    'numpy', 'matplotlib', 'requests', 'flask',
    'pandas', 'scikit-learn', 'beautifulsoup4', 'tensorflow',
    'django', 'pytest', 'pillow', 'sqlalchemy',
    'pyqt5', 'opencv-python', 'pyyaml', 'pytest-cov',
    'pyinstaller', 'jupyter', 'tweepy', 'pytorch',
    'selenium', 'kivy', 'pygame', 'networkx',
    'pyglet', 'plotly', 'dash', 'streamlit',
    'pytz', 'geopy', 'bokeh', 'folium',
    'flask-restful', 'flask-cors', 'scrapy', 'requests-html',
    'matplotlib-venn', 'wordcloud', 'pylint', 'autopep8',
    'flask-RESTful', 'fastapi', 'pydantic', 'uvicorn',
    'gunicorn', 'pydub', 'pyinstaller', 'pywebview',
    'pyautogui', 'pyjokes', 'tqdm', 'pycryptodome',
    'pandas-profiling', 'pyqtgraph', 'dash-bootstrap-components', 'dash-core-components',
    'dash-html-components', 'dash-renderer', 'dash-table', 'cx_Freeze',
    'cryptography', 'pyzmq', 'pymongo', 'scipy', 'scrapy-splash',
    'sqlparse', 'statsmodels', 'sympy', 'twisted',
    'uproot', 'urlib3', 'validators', 'virtualenv',
    'websocket-client', 'werkzeug', 'whoosh', 'xarray',
    'xlrd', 'xlsxwriter', 'xlwt', 'xmltodict',
    'yagmail', 'yellowbrick', 'zarr', 'zict',
    'zipp', 'zope.interface'
]

# GUI setup
root = Tk()
root.title("Package Installer")

# Styling
root.geometry("500x400")
root.configure(bg='#8A2BE2')  # Set root window background color

font_style = font.Font(family="Helvetica", size=12)

# Frame
main_frame = Frame(root, padx=20, pady=20, bg='#8A2BE2')  # Set frame background color
main_frame.pack(expand=True, fill="both")

# Dropdown menu
package_var = StringVar()
package_dropdown = ttk.Combobox(main_frame, textvariable=package_var, values=available_packages, state="readonly", font=font_style)
package_dropdown.grid(row=0, column=0, padx=10, pady=10)

# Install button
install_button = Button(main_frame, text="Install Selected Package", command=on_install_button_click, font=font_style)
install_button.grid(row=1, column=0, pady=10)

# Instructions label
instructions_label = Label(main_frame, text="Select a package from the dropdown and click 'Install'.", font=font_style, wraplength=400, bg='#8A2BE2')  # Set label background color
instructions_label.grid(row=2, column=0, pady=10)

# Feedback section
feedback_frame = Frame(root, padx=20, pady=20, bg='#8A2BE2')  # Set frame background color
feedback_frame.pack(expand=True, fill="both")

# Username entry
username_label = Label(feedback_frame, text="Username:", font=font_style, bg='#8A2BE2')  # Set label background color
username_label.grid(row=0, column=0, pady=10)

username_var = StringVar()
username_entry = Entry(feedback_frame, textvariable=username_var, font=font_style)
username_entry.grid(row=0, column=1, pady=10)

# Feedback entry
feedback_label = Label(feedback_frame, text="Feedback:", font=font_style, bg='#8A2BE2')  # Set label background color
feedback_label.grid(row=1, column=0, pady=10)

feedback_entry = Text(feedback_frame, width=40, height=5, font=font_style)
feedback_entry.grid(row=1, column=1, pady=10)

submit_feedback_button = Button(feedback_frame, text="Submit Feedback", command=submit_feedback, font=font_style)
submit_feedback_button.grid(row=2, column=0, columnspan=2, pady=10)

feedback_display = Text(feedback_frame, width=40, height=10, state="disabled", font=font_style)
feedback_display.grid(row=3, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()

