import random
index_max = 100
stars = []

for _ in range(100):
    star = [random.randint(0, 640), random.randint(0, 480)] 
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
    
    while index < index_max:
        if stars_x[index] > 640:
            stars_x.pop(index)
            stars_y.pop(index)
            index_max -= 1
        else:
            ellipse(stars_x[index], stars_y[index], 5, 5)
            stars_x[index] += 0.2
            index += 1
            
    if frameCount % 60 == 0:
        stars_x.append(random.randint(-10, 0))
        stars_y.append(random.randint(0, 480))
        index_max += 1
    
   
