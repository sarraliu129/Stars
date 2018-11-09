import random
index_max = 100
stars = []

for i in range(100):
    star = ([random.randint(0, 640), random.randint(0, 480)])
    stars += star
    
    
def setup():
    size(640, 480)


def draw():
    background(0)
    global index, index_max
    
    # draw stars
    noStroke()
    fill(255)
    

    index = 0

        
    for star in stars:
        if star[0] >= 640:
            star.pop(index)
            index_max -= 1
        else:
            ellipse(star[0], star[1], 5, 5)
            star[0] += 0.2
            index += 1
            
    if frameCount % 60 == 0:
        stars.append([random.randint(-10, 0), random.randint(0, 480)])
        index_max += 1
    
   
