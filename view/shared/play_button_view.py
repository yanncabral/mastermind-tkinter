def play_button_view(canvas, *, column, row, padding_x=32, padding_y=32, color, **kwargs):
    i, j, px, py = column, row, padding_x/2, padding_y/2
    return canvas.create_polygon(
        50 * i + px, 50 * j + py, 

        50 * i + px, 50 * (j+1) - py, 

        50 * (i+1) - px, 50 * (j+0.5), 
        fill=color, 
        outline=color,
        width=2,
        **kwargs
    )