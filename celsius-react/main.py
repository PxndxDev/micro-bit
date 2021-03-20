def clear_screen():
    Xs = [
      0, 0, 0, 0, 0,
      1, 1, 1, 1, 1,
      2, 2, 2, 2, 2,
      3, 3, 3, 3, 3,
      4, 4, 4, 4, 4
    ];
    Ys = [
      0, 1, 2, 3, 4,
      0, 1, 2, 3, 4,
      0, 1, 2, 3, 4,
      0, 1, 2, 3, 4,
      0, 1, 2, 3, 4
    ];
    i = 0
    while i < 25:
        led.unplot(Xs[i], Ys[i])
        i = i + 1

def on_forever():
    if input.temperature() < 40:
        clear_screen()
        Xs = [ 0, 1, 2, 3, 4 ]
        Ys = [ 3, 4, 3, 2, 1 ]
        indice = 0
        while indice < 5:
            led.plot(Xs[indice], Ys[indice])
            indice = indice + 1
    elif input.temperature() > 40:
        clear_screen()
        Xs = [ 0, 2, 4, 0, 2, 4, 0, 2, 4, 0, 2, 4 ]
        Ys = [ 0, 0, 0, 1, 1, 1, 2, 2, 2, 4, 4, 4 ]
        indice = 0
        while indice < 12:
            led.plot(Xs[indice], Ys[indice])
            indice = indice + 1
basic.forever(on_forever)
