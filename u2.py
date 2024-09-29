import keyboard
import pyperclip
import json
import random
from pathlib import Path

# Global list to store clipboard contents
clipboard_list = []

template_str2 = "Hello {}! I'm from Reobrix, a top Chinese building block brand. Let's connect and explore potential collaborations together!"
template_str1 = "Hello {}! I'm from Reobrix, a top Chinese building block brand. We are looking for MOC designers to cooperate, can we talk?"


def save_clipboard():
    """Save the current clipboard content to the global list."""
    content = pyperclip.paste().strip()
    clipboard_list.append(content)
    print(f"Saved: {content}")

def copy_list_to_clipboard(numbered=False):
    """Copy the contents of the list to the clipboard, optionally with numbered bullets."""
    if numbered:
        content = "\n".join(f"{i+1}. {item}" for i, item in enumerate(clipboard_list))
    else:
        content = "\n".join(clipboard_list)
    pyperclip.copy(content)
    print("All items copied to clipboard")

def clear_list():
    """Clear the global list."""
    clipboard_list.clear()
    print("List cleared")

def continuously_copy():
    """Set up hotkeys and keep the script running."""
    # Set hotkeys
    keyboard.add_hotkey('alt+z', save_clipboard)
    keyboard.add_hotkey('ctrl+f1', lambda: copy_list_to_clipboard(numbered=False))
    keyboard.add_hotkey('ctrl+f2', lambda: copy_list_to_clipboard(numbered=True))
    keyboard.add_hotkey('ctrl+f3', clear_list)

    print("Hotkeys set up: 'alt+z' to save clipboard, 'Ctrl+F1' to copy list to clipboard, 'Ctrl+F2' to copy numbered list to clipboard, 'Ctrl+F3' to clear list.")
    print("Press 'Ctrl+Esc' to exit.")

    # Keep the script running
    keyboard.wait('ctrl+esc')


def process_template():
    """Process the clipboard content with the template and copy it back to the clipboard."""
    content = pyperclip.paste().strip()
    path = Path("words.json")
    path_txt = path.read_text()
    templates = json.loads(path_txt)["moc_greeting"]
    print("List items: ",len(templates))
    template_str = random.choice(templates)
    templated_content = template_str.format(content)
    pyperclip.copy(templated_content)
    print(f"Template applied: {templated_content}")


def templated_copy():
    """Wait for 'ctrl+c+x' and embed clipboard content into a template string."""
    keyboard.add_hotkey('ctrl+c+x', process_template)
    print("Press 'Ctrl+c+x' to process the template and 'ctrl+esc' to exit.")
    keyboard.wait('ctrl+esc')
    print("Exited.")


# Call the function to start the process
continuously_copy()
# templated_copy()



