web_development = ["Rahul", "Sneha", "Vikram"]
data_science = ["Anita", "Kiran", "Suresh"]
ui_ux_design = ["Priya", "Manoj", "Leena"]
all_participants = [web_development, data_science, ui_ux_design]
web_development.append("Ravi")
data_science.insert(1, "Neha")
ui_ux_design.pop()
copied_data_science = data_science.copy()
data_science.clear()
print("First two Web Development participants:", web_development[:2])
name_lengths = [len(name) for name in copied_data_science]
print("Length of each name in copied Data Science list:", name_lengths)
asha_present = ("Asha" in web_development) or ("Asha" in copied_data_science) or ("Asha" in ui_ux_design)
print("Is 'Asha' in any workshop list?", asha_present)
first_participants = (web_development[0], copied_data_science[0], ui_ux_design[0])
print("Tuple of first participants:", first_participants)