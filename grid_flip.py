"""
A dumb version of something I saw on JvR's lecture: https://vimeo.com/230514302
"""

from _lib.drawShapes import cRect

PAGESIZE = 500
CELLSIZE = 50
FRAMES   = 10
TURNS    = 8
ROWS     = 8
COLS     = 8

for turn in range(TURNS):
    for frame in range(FRAMES+1):
        f = frame / FRAMES
        newPage(PAGESIZE, PAGESIZE)
        
        #canvas
        fill(1)
        rect(0, 0, PAGESIZE, PAGESIZE)

        #squares
        translate(CELLSIZE/3, CELLSIZE/3) # margin
        for row in range(ROWS):
            save()
            for col in range(COLS):
                fill(1, col / COLS, row / ROWS, 1)
                
                newPath()
                
                if turn == 0:
                    moveTo((0, f * CELLSIZE))
                    lineTo((0, CELLSIZE))
                    lineTo((CELLSIZE, CELLSIZE))
                    lineTo((CELLSIZE, 0))
                
                elif turn == 1:
                    moveTo((0, CELLSIZE))
                    lineTo((CELLSIZE, CELLSIZE))
                    lineTo((CELLSIZE, 0))
                    lineTo((CELLSIZE - f * CELLSIZE, 0))

                elif turn == 2:
                    moveTo((f * CELLSIZE, CELLSIZE))
                    lineTo((CELLSIZE, CELLSIZE))
                    lineTo((CELLSIZE, 0))
                    lineTo((0, 0))

                elif turn == 3:
                    moveTo((0, 0))
                    lineTo((0, f * CELLSIZE))
                    lineTo((CELLSIZE, CELLSIZE))
                    lineTo((CELLSIZE, 0))
                
                elif turn == 4:
                    moveTo((0, 0))
                    lineTo((0, CELLSIZE))
                    lineTo((CELLSIZE, CELLSIZE - f * CELLSIZE))
                    lineTo((CELLSIZE, 0))

                elif turn == 5:
                    moveTo((0, 0))
                    lineTo((0, CELLSIZE))
                    lineTo((f * CELLSIZE, CELLSIZE))
                    lineTo((CELLSIZE, 0))
                
                elif turn == 6:
                    moveTo((0, 0))
                    lineTo((0, CELLSIZE))
                    lineTo((CELLSIZE, CELLSIZE))
                    lineTo((CELLSIZE - f * CELLSIZE, 0))
                
                elif turn == 7:
                    moveTo((0, 0))
                    lineTo((0, CELLSIZE))
                    lineTo((CELLSIZE, CELLSIZE))
                    lineTo((CELLSIZE, CELLSIZE - f * CELLSIZE))

                closePath()
                drawPath()
                translate(CELLSIZE * 1.1875, 0) # gutter between columns

            restore()
            
            translate(0, CELLSIZE * 1.1875) # gutter between rows

saveImage("_gifs/grid_flip.gif")