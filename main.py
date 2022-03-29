Ex 3 

def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_icon(IconNames.HAPPY)
    else:
        if input.button_is_pressed(Button.B):
            basic.show_icon(IconNames.SAD)
basic.forever(on_forever)


ex 4 

_var = 0

def on_forever():
    global _var
    _var = 0
    while _var < 9 and _var / 2 != 0:
        var1 = 0
        _var = var1
        basic.show_number(var1)
basic.forever(on_forever)


Ex 5 
_var = 0
for index in range(9):
    if _var % 2 == 1:
        basic.show_number(_var)
    _var += 1