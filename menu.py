import customtkinter as ctk
import config 
import subprocess 
import os

app = ctk.CTk()
app.title("Ares Menu")
app.geometry("900x750")


def run_and_close():
    print("Started Running 'main_tensorrt.py'")
    selected_model = model_selector.get()
    subprocess.Popen(['python', 'main_tensorrt.py', selected_model])
    app.quit()

def get_engine_files():
    return [f for f in os.listdir() if f.endswith('.engine')]

def create_model_selector(parent, row, column, engine_files, default_model):
    ctk.CTkLabel(parent, text="Select Model").grid(row=row, column=column, pady=(10, 0), padx=(10, 0), sticky="w")
    model_selector = ctk.CTkComboBox(parent, values=engine_files)
    model_selector.set(default_model)
    model_selector.grid(row=row, column=column + 1, pady=(10, 0), padx=(10, 10), sticky="w")
    return model_selector



# def create seperator
def create_section_title(parent, title, row, columnspan):
    title_frame = ctk.CTkFrame(parent, height=30, corner_radius=10)
    title_frame.grid(row=row, column=0, columnspan=columnspan, pady=(10, 0), sticky="ew")
    
    title_frame.grid_propagate(False)  
    title_frame.columnconfigure(0, weight=1)
    
    title_label = ctk.CTkLabel(title_frame, text=title)
    title_label.grid(row=0, column=0, sticky="ew")
    
    title_label.place(relx=0.5, rely=0.5, anchor="center")
    
def create_setting_widget(parent, label, row, column, widget_type=ctk.CTkEntry, **options):
    ctk.CTkLabel(parent, text=label).grid(row=row, column=column, pady=(10, 0), padx=(10, 0), sticky="w")
    if widget_type == ctk.CTkCheckBox and 'text' not in options:
        options['text'] = ""
    widget = widget_type(parent, **options)
    widget.grid(row=row, column=column + 1, pady=(10, 0), padx=(10, 10), sticky="w")
    return widget

# create frame
frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

def set_initial_values(entry_widget, config_value):
    entry_widget.insert(0, str(config_value))

def set_checkbox(checkbox, value):
    if hasattr(checkbox, 'get'):
        current_value = checkbox.get()
        if current_value != value:  
            if value:
                checkbox.select()
            else:
                checkbox.deselect()


frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)

screen_settings_start_row = 0
mask_settings_start_row = screen_settings_start_row + 3
game_aim_settings_start_row = mask_settings_start_row + 4
advanced_settings_start_row = game_aim_settings_start_row + 5
hardware_settings_start_row = advanced_settings_start_row + 4

# Screen Settings Section
create_section_title(frame, "Screen Settings", screen_settings_start_row, 4)
screen_shot_height_entry = create_setting_widget(frame, "Screen Shot Height", screen_settings_start_row + 1, 0)
screen_shot_width_entry = create_setting_widget(frame, "Screen Shot Width", screen_settings_start_row + 1, 2)

# Mask Settings Section
create_section_title(frame, "Mask Settings", mask_settings_start_row, 4)
use_mask_checkbox = create_setting_widget(frame, "Use Mask", mask_settings_start_row + 1, 0, widget_type=ctk.CTkCheckBox)
mask_width_entry = create_setting_widget(frame, "Mask Width", mask_settings_start_row + 1, 2)
mask_height_entry = create_setting_widget(frame, "Mask Height", mask_settings_start_row + 2, 0)

# Game & Aim Settings Section
create_section_title(frame, "Game & Aim Settings", game_aim_settings_start_row, 4)
auto_game_detection_checkbox = create_setting_widget(frame, "Automatic Game Detection", game_aim_settings_start_row + 1, 0, widget_type=ctk.CTkCheckBox)
game_name_entry = create_setting_widget(frame, "Game Name", game_aim_settings_start_row + 1, 2)
aa_movement_amp_entry = create_setting_widget(frame, "Aim.Bot Sensitivity", game_aim_settings_start_row + 2, 0)
confidence_entry = create_setting_widget(frame, "Aim Confidence", game_aim_settings_start_row + 2, 2)
fov_circle_size_entry = create_setting_widget(frame, "FOV Circle Size", game_aim_settings_start_row + 3, 0)
body_part_selector = create_setting_widget(frame, "Body Part Selector", game_aim_settings_start_row + 4, 0, widget_type=ctk.CTkComboBox, values=["Head", "Neck", "Body", "Pelvis"])
body_part_selector.set(config.BodyPart)
random_body_part_checkbox = create_setting_widget(frame, "Randomized Body Part", game_aim_settings_start_row + 3, 2, widget_type=ctk.CTkCheckBox)
random_body_part_checkbox.grid(row=game_aim_settings_start_row + 3, column=3, pady=(10, 0), padx=(10, 10), sticky="w")
center_of_screen_checkbox = create_setting_widget(frame, "Center of Screen Selection", game_aim_settings_start_row + 5, 0, widget_type=ctk.CTkCheckBox)


# Advanced Settings Section, including the Model Selector
create_section_title(frame, "Advanced Settings", advanced_settings_start_row, 4)
aa_quit_key_entry = create_setting_widget(frame, "Autoaim Quit Key", advanced_settings_start_row + 1, 0)
cps_display_checkbox = create_setting_widget(frame, "Display CPS", advanced_settings_start_row + 1, 2, widget_type=ctk.CTkCheckBox)
visuals_checkbox = create_setting_widget(frame, "Enable Visuals", advanced_settings_start_row + 2, 0, widget_type=ctk.CTkCheckBox)

engine_files = get_engine_files()
model_selector = create_model_selector(frame, advanced_settings_start_row + 2, 2, engine_files, config.selectedModel)

# Hardware Settings Section
create_section_title(frame, "Hardware Settings", hardware_settings_start_row, 4)
arduino_leonardo_checkbox = create_setting_widget(frame, "Use Arduino Leonardo", hardware_settings_start_row + 1, 0, widget_type=ctk.CTkCheckBox)
arduino_port_entry = create_setting_widget(frame, "Arduino Port", hardware_settings_start_row + 1, 2)
onnx_choice_entry = create_setting_widget(frame, "ONNX Choice (1-CPU, 2-AMD, 3-NVIDIA)", hardware_settings_start_row + 2, 0)

set_initial_values(screen_shot_height_entry, config.screenShotHeight)
set_initial_values(screen_shot_width_entry, config.screenShotWidth)
set_initial_values(mask_width_entry, config.maskWidth)
set_initial_values(mask_height_entry, config.maskHeight)
set_initial_values(game_name_entry, config.gameName)
set_initial_values(aa_movement_amp_entry, config.aaMovementAmp)
set_initial_values(confidence_entry, config.confidence)
set_initial_values(fov_circle_size_entry, config.fovCircleSize)
set_initial_values(aa_quit_key_entry, config.aaQuitKey)
set_initial_values(onnx_choice_entry, config.onnxChoice)
set_initial_values(arduino_port_entry, config.arduinoPort)

use_mask_checkbox = create_setting_widget(frame, "Use Mask", 4, 0, widget_type=ctk.CTkCheckBox, text="")


set_checkbox(use_mask_checkbox, config.useMask)
set_checkbox(auto_game_detection_checkbox, config.autoGameDetection)
set_checkbox(cps_display_checkbox, config.cpsDisplay)
set_checkbox(visuals_checkbox, config.visuals)
set_checkbox(center_of_screen_checkbox, config.centerOfScreen)
set_checkbox(arduino_leonardo_checkbox, config.ArduinoLeonardo)
set_checkbox(random_body_part_checkbox, config.RandomBodyPart) 

# self explanatory save settings
def save_settings():
    selected_model = model_selector.get()
    use_mask_value = use_mask_checkbox.get() == 1
    auto_game_detection_value = auto_game_detection_checkbox.get() == 1
    cps_display_value = cps_display_checkbox.get() == 1
    visuals_value = visuals_checkbox.get() == 1
    center_of_screen_value = center_of_screen_checkbox.get() == 1
    arduino_leonardo_value = arduino_leonardo_checkbox.get() == 1

    # save to config.py
    with open('config.py', 'w') as config_file:
        config_file.write(f"screenShotHeight = {screen_shot_height_entry.get()}\n")
        config_file.write(f"screenShotWidth = {screen_shot_width_entry.get()}\n")
        config_file.write(f"useMask = {use_mask_value}\n")
        config_file.write(f"maskWidth = {mask_width_entry.get()}\n")
        config_file.write(f"maskHeight = {mask_height_entry.get()}\n")
        config_file.write(f"autoGameDetection = {auto_game_detection_value}\n")
        config_file.write(f"gameName = '{game_name_entry.get()}'\n")
        config_file.write(f"aaMovementAmp = {float(aa_movement_amp_entry.get())}\n")
        config_file.write(f"confidence = {float(confidence_entry.get())}\n")
        config_file.write(f"fovCircleSize = {fov_circle_size_entry.get()}\n")
        config_file.write(f"aaQuitKey = '{aa_quit_key_entry.get()}'\n")
        config_file.write(f"cpsDisplay = {cps_display_value}\n")
        config_file.write(f"visuals = {visuals_value}\n")
        config_file.write(f"centerOfScreen = {center_of_screen_value}\n")
        config_file.write(f"onnxChoice = {int(onnx_choice_entry.get())}\n")
        config_file.write(f"ArduinoLeonardo = {arduino_leonardo_value}\n")
        config_file.write(f"arduinoPort = '{arduino_port_entry.get()}'\n")
        config_file.write(f"selectedModel = '{selected_model}'\n") 
        config_file.write(f"BodyPart = '{body_part_selector.get()}'\n")
        random_body_part_value = random_body_part_checkbox.get() == 1
        config_file.write(f"RandomBodyPart = {random_body_part_value}\n")
    print("Settings saved")

buttons_frame = ctk.CTkFrame(app)
buttons_frame.pack(pady=20, fill="x")

save_button = ctk.CTkButton(buttons_frame, text="Save Settings", command=save_settings)
save_button.grid(row=0, column=0, padx=10, sticky="ew")

run_button = ctk.CTkButton(buttons_frame, text="Run", command=run_and_close)
run_button.grid(row=0, column=1, padx=10, sticky="ew")

buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=1)

app.mainloop()
