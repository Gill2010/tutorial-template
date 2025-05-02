def on_in_background():
    basic.show_string("Hello!")
    music.play_melody("A G E G A G E G ", 120)
    led.set_display_mode(DisplayMode.BLACK_AND_WHITE)
control.in_background(on_in_background)
