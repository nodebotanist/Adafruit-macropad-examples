import time
from adafruit_macropad import MacroPad
import buttonConfigs


macropad = MacroPad()
text_lines = macropad.display_text(title="Hello, World!")
current_layer = 0

while (True):
    key_event = macropad.keys.events.get()
    if key_event and key_event.pressed:
        color = buttonConfigs.BUTTON_CONFIGS[current_layer][key_event.key_number][0]
        commands = buttonConfigs.BUTTON_CONFIGS[current_layer][key_event.key_number][1]
        for command in commands:
            eval(command)
    time.sleep(0.2)