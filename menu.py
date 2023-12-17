# Imports


# Don't have to use "customtkinter." infront of everything
from customtkinter import *

import subprocess

import config




# App


app = CTk()  # Create CTk window
app.title("AI Aimbot Experimental Features") # App title
app.geometry("900x750")


# A little transparent doesn't hurt
#app.attributes("-alpha", 0.9) #TODO transparent switch


# No resize >:(
app.resizable(False, False)


set_appearance_mode("Dark")  # Modes: system (default), light, dark




#TODO theme switcher
# NeonBanana MoonlitSky GhostTrain Oceanix Sweetkind LightMode Hades // 
set_default_color_theme('./themes/SweetkindClean.json')




# Functions


# Run main_tensorrt.py then close gui
def run_aimbot(): # Run main_tensorrt.py and close the gui
    print("Started Running 'main_tensorrt.py'")
    subprocess.Popen(['python', 'main_tensorrt.py'])
    app.quit()


# def create frame and label seperators
def create_frame_label(parent, title, row, columnspan):
    title_frame = CTkFrame(parent, height=30, corner_radius=10)
    title_frame.grid(row=row, column=0, columnspan=columnspan, pady=(10, 0), padx=(10, 10), sticky="ew")
    
    title_frame.grid_propagate(False)  
    title_frame.columnconfigure(0, weight=1)
    
    title_label = CTkLabel(title_frame, text=title)
    title_label.grid(row=0, column=0, sticky="ew")
    
    title_label.place(relx=0.5, rely=0.5, anchor="center")


# def create widgets
def create_setting_widget(parent, label, row, column, widget_type=CTkEntry, **options):
    CTkLabel(parent, text=label).grid(row=row, column=column, pady=(10, 0), padx=(46, 0), sticky="w")
    if widget_type == CTkCheckBox and 'text' not in options:
        options['text'] = ""
    widget = widget_type(parent, **options)
    widget.grid(row=row, column=column + 1, pady=(10, 0), padx=(10, 10), sticky="w")
    return widget


# def create button widget
def create_button_widget(parent, text, row, columnspan, command):
    button_frame = CTkFrame(parent, height=30, corner_radius=10)
    button_frame.grid(row=row, column=0, columnspan=columnspan, pady=(15, 0), padx=(10, 10), sticky="ew")

    button_frame.grid_propagate(False)  
    button_frame.columnconfigure(0, weight=1)

    button = CTkButton(button_frame, text=text, height=30, command=command)
    button.grid(row=0, column=0, sticky="ew")


def create_combobox(parent, text, row, column, options, default):
    CTkLabel(parent, text=text).grid(row=row, column=column, pady=(10, 0), padx=(10, 0), sticky="w")
    combobox = CTkComboBox(parent, values=options)
    combobox.set(default)
    combobox.grid(row=row, column=column + 1, pady=(10, 0), padx=(10, 10), sticky="w")
    return combobox


# def set intitial values for config - BetterSnomn
def set_initial_values(entry_widget, config_value):
    entry_widget.insert(0, str(config_value))


# def set checkbox value for config - BetterSnomn
def set_checkbox(checkbox, value):
    if hasattr(checkbox, 'get'):
        current_value = checkbox.get()
        if current_value != value:  
            if value:
                checkbox.select()
            else:
                checkbox.deselect()


# Save settings to config
def save_settings():
    use_mask_value = use_mask_checkbox.get() == 1
    auto_game_detection_value = auto_game_detection_checkbox.get() == 1
    use_fov_circle_value = use_fov_circle_checkbox.get() == 1
    center_of_screen_value = center_of_screen_checkbox.get() == 1
    headshot_mode_value = headshot_mode_checkbox.get() == 1
    cps_display_value = cps_display_checkbox.get() == 1
    visuals_value = visuals_checkbox.get() == 1


    # save to config.py (Aimbot uses config.py or else it would be called damn settings.py)
    with open('config.py', 'w') as config_file:
        config_file.write(f"screenShotHeight = {screen_shot_height_entry.get()}\n")
        config_file.write(f"screenShotWidth = {screen_shot_width_entry.get()}\n")
        config_file.write(f"useMask = {use_mask_value}\n")
        config_file.write(f"maskSide = '{mask_side_entry.get()}'\n")
        config_file.write(f"maskWidth = {mask_width_entry.get()}\n")
        config_file.write(f"maskHeight = {mask_height_entry.get()}\n")
        config_file.write(f"autoGameDetection = {auto_game_detection_value}\n")
        config_file.write(f"gameName = '{game_name_entry.get()}'\n")
        config_file.write(f"aaMovementAmp = {float(aa_movement_amp_entry.get())}\n")
        config_file.write(f"confidence = {float(confidence_entry.get())}\n")
        config_file.write(f"fovCircle = {use_fov_circle_value}\n")
        config_file.write(f"fovCircleSize = {fov_circle_size_entry.get()}\n")
        config_file.write(f"headshotMode = {headshot_mode_value}\n")
        config_file.write(f"aaQuitKey = '{aa_quit_key_entry.get()}'\n")
        config_file.write(f"cpsDisplay = {cps_display_value}\n")
        config_file.write(f"visuals = {visuals_value}\n")
        config_file.write(f"centerOfScreen = {center_of_screen_value}\n")
        config_file.write(f"onnxChoice = {int(onnx_choice_entry.get())}\n")
    print("Settings saved")




# Creating background frame for stacking effect :)
bg_frame = CTkFrame(app)
bg_frame.pack(fill="both", expand=True)




# Top bar #TODO profile menu like yes :/
top_bar_label = CTkLabel(bg_frame, text="AI Aimbot Experimental Features", font=("Arial", 14))
top_bar_label.place(relx=0.02, rely=0.01)




# Creating tabs
tabs = CTkTabview(bg_frame)
tabs.pack(padx=30, pady=30, fill="both", expand=True)

# Tab names
tabs.add("Welcome")
tabs.add("Aimbot")
tabs.add("Settings")




## Welcome Tab






## Aimbot Tab
    



# Creating frame ontop of tabs
aimbot_frame_on_tabview = CTkFrame(tabs.tab("Aimbot"))
aimbot_frame_on_tabview.pack(padx=20, pady=20, fill="both", expand=True)

# settings_frame_on_tabview columns
aimbot_frame_on_tabview.columnconfigure(0, weight=1)
aimbot_frame_on_tabview.columnconfigure(1, weight=1)
aimbot_frame_on_tabview.columnconfigure(2, weight=1)
aimbot_frame_on_tabview.columnconfigure(3, weight=1)

# Frame rows
aimbot_launch_options_row = 0
aimbot_run_row = aimbot_launch_options_row + 3




# Launcher Options
create_frame_label(aimbot_frame_on_tabview, "Aimbot Options", aimbot_launch_options_row, 4)

launch_options = ['main_tensorrt.py', 'main_onnx.py']
create_combobox(aimbot_frame_on_tabview, "Select Launch Option", 1, 0, launch_options, launch_options[0])




# Run Aimbot Button
create_button_widget(aimbot_frame_on_tabview, "Run Aimbot", aimbot_run_row, 4, run_aimbot)




## Settings Tab




# Creating frame ontop of tabs
settings_frame_on_tabview = CTkFrame(tabs.tab("Settings"))
settings_frame_on_tabview.pack(padx=20, pady=20, fill="both", expand=True)

# settings_frame_on_tabview columns
settings_frame_on_tabview.columnconfigure(0, weight=1)
settings_frame_on_tabview.columnconfigure(1, weight=1)
settings_frame_on_tabview.columnconfigure(2, weight=1)
settings_frame_on_tabview.columnconfigure(3, weight=1)

# Frame rows
screen_settings_row = 0
mask_settings_row = screen_settings_row + 3
game_settings_row = mask_settings_row + 4
aim_settings_row = game_settings_row + 5
advanced_settings_row = aim_settings_row + 4
buttons_row = advanced_settings_row + 3




# Screen Settings Section   #Parent, Title, Row, Column
create_frame_label(settings_frame_on_tabview, "Screen Settings", screen_settings_row, 4)
screen_shot_height_entry = create_setting_widget(settings_frame_on_tabview, "Screen Shot Height", screen_settings_row + 1, 0)
screen_shot_width_entry = create_setting_widget(settings_frame_on_tabview, "Screen Shot Width", screen_settings_row + 1, 2)




# Mask Settings Section
create_frame_label(settings_frame_on_tabview, "Mask Settings", mask_settings_row, 4)
use_mask_checkbox = create_setting_widget(settings_frame_on_tabview, "Use Mask", mask_settings_row + 1, 0, widget_type=CTkCheckBox)
mask_side_entry = create_setting_widget(settings_frame_on_tabview, "Mask Side", mask_settings_row + 1, 2)
mask_width_entry = create_setting_widget(settings_frame_on_tabview, "Mask Width", mask_settings_row + 2, 0)
mask_height_entry = create_setting_widget(settings_frame_on_tabview, "Mask Height", mask_settings_row + 2, 2)




# Game Settings Section
create_frame_label(settings_frame_on_tabview, "Game Settings", game_settings_row, 4)
auto_game_detection_checkbox = create_setting_widget(settings_frame_on_tabview, "Automatic Game Detection", game_settings_row + 1, 0, widget_type=CTkCheckBox)
game_name_entry = create_setting_widget(settings_frame_on_tabview, "Game Name", game_settings_row + 1, 2)




# Aim Settings Section
create_frame_label(settings_frame_on_tabview, "Aim Settings", aim_settings_row, 4)
aa_movement_amp_entry = create_setting_widget(settings_frame_on_tabview, "Aimbot Amp", aim_settings_row + 1, 0)
confidence_entry = create_setting_widget(settings_frame_on_tabview, "Aim Confidence", aim_settings_row + 1, 2)
use_fov_circle_checkbox = create_setting_widget(settings_frame_on_tabview, "FOV Circle", aim_settings_row + 2, 0, widget_type=CTkCheckBox)
fov_circle_size_entry = create_setting_widget(settings_frame_on_tabview, "FOV Circle Size", aim_settings_row + 2, 2)
center_of_screen_checkbox = create_setting_widget(settings_frame_on_tabview, "Center of Screen Selection", aim_settings_row + 3, 0, widget_type=CTkCheckBox)
headshot_mode_checkbox = create_setting_widget(settings_frame_on_tabview, "Headshot Mode", aim_settings_row + 3, 2, widget_type=CTkCheckBox)




# Advanced Settings Section, including the Model Selector
create_frame_label(settings_frame_on_tabview, "Advanced Settings", advanced_settings_row, 4)
aa_quit_key_entry = create_setting_widget(settings_frame_on_tabview, "Autoaim Quit Key", advanced_settings_row + 1, 0)
cps_display_checkbox = create_setting_widget(settings_frame_on_tabview, "Display CPS", advanced_settings_row + 1, 2, widget_type=CTkCheckBox)
onnx_choice_entry = create_setting_widget(settings_frame_on_tabview, "ONNX Choice (1-CPU, 2-AMD, 3-NVIDIA)", advanced_settings_row + 2, 0)
visuals_checkbox = create_setting_widget(settings_frame_on_tabview, "Enable Visuals", advanced_settings_row + 2, 2, widget_type=CTkCheckBox)




# Config shiz
set_initial_values(screen_shot_height_entry, config.screenShotHeight)
set_initial_values(screen_shot_width_entry, config.screenShotWidth)
set_initial_values(mask_side_entry, config.maskSide)
set_initial_values(mask_width_entry, config.maskWidth)
set_initial_values(mask_height_entry, config.maskHeight)
set_initial_values(game_name_entry, config.gameName)
set_initial_values(aa_movement_amp_entry, config.aaMovementAmp)
set_initial_values(confidence_entry, config.confidence)
set_initial_values(fov_circle_size_entry, config.fovCircleSize)
set_initial_values(aa_quit_key_entry, config.aaQuitKey)
set_initial_values(onnx_choice_entry, config.onnxChoice)


# Checkbox config shiz
set_checkbox(use_mask_checkbox, config.useMask)
set_checkbox(auto_game_detection_checkbox, config.autoGameDetection)
set_checkbox(use_fov_circle_checkbox, config.fovCircle)
set_checkbox(center_of_screen_checkbox, config.centerOfScreen)
set_checkbox(headshot_mode_checkbox, config.headshotMode)
set_checkbox(cps_display_checkbox, config.cpsDisplay)
set_checkbox(visuals_checkbox, config.visuals)




# Save Settings
create_button_widget(settings_frame_on_tabview, "Save Settings", buttons_row, 4, save_settings)






# Render app
app.mainloop()