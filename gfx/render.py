def render(array, window):
    window.fill((66, 194, 244))
    for x in range (len(array)):
        array[x].render(window)