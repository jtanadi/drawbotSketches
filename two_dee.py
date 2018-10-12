FRAMES = 35
ROWS = 36 
COLS = 13
font("Skia", 19)
for axis, data in listFontVariations().items():
    print((axis, data))

for frame in range(FRAMES):
    newPage(1280, 800)
    fill(0, 0, 0)
    rect(0, 0, 1280, 800)

    fill(1, 1, 1)
    font("Skia", 19)

    for col in range(COLS + 1):
        for row in range(ROWS):
            weight = abs(abs(row - frame)-frame) / (row+1) * 3

            fontVariations(wght=weight)
            
            if row % 2 == 0:
                text("TWO", (-57.5 + col * 100, -55 + row * 25))
                text("DEE", (-5 + col * 100, -55 + row * 25))
            else:
                text("TWO", (-7.5 + col * 100, -55 + row * 25))
                text("DEE", (-55 + col * 100, -55 + row * 25))
    
saveImage(u"~/Dropbox/two_dee.mp4")
