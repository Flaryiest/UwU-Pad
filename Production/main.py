from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import MatrixScanner
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode, OledReactionType
from kmk.extensions.rgb import RGB
import board

keyboard = KMKKeyboard()


keyboard.col_pins = (board.GP03, board.GP04, board.GP02, board.GP01)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28)


keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.Q, KC.W, KC.E, KC.R],   
    [KC.A, KC.S, KC.D, KC.F], 
    [KC.Z, KC.X, KC.C, KC.V],
]

rgb = RGB(
    pixel_pin=board.GP06,
    num_pixels=4,
    val_limit=100,  
    hue_default=180,
    sat_default=255,
    val_default=80,
    animation_speed=2,
)
keyboard.extensions.append(rgb)

if __name__ == '__main__':
    keyboard.go()