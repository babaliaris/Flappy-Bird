#Sprite Class

class Sprite:

    def __init__(this, image, start_pos = (0,0)):

        this.image = image
        this.pos   = start_pos
        this.gravity = False
        this.gravity_speed = 5



    def set_image(this, new_imgage):

        this.image = new_imgage


    def set_pos(this, new_pos):

        this.pos = new_pos


    def set_gravity(this, value, speed):

        this.gravity = True
        this.gravity_speed = speed


    def render(this, screen, gravity_active = False):

        x, y = this.pos

        screen.blit(this.image, this.pos)

        if (this.gravity and gravity_active):
            y += this.gravity_speed
            this.pos = (x, y)



    def get_image(this):

        return this.image


    def get_pos(this):

        return this.pos


    def get_width(this):

        return this.image.get_width()


    def get_height(this):

        return this.image.get_height()



    def move(this, speed, left = False, up = False):

        x, y = this.pos

        if (left):
            x -= speed

        elif (up):
            y -= speed

        this.pos = (x, y)


    def get_collision(this, other):

        x1, y1 = this.pos
        x2, y2 = other.get_pos()

        if (x1 + this.get_width() >= x2 and x1 + this.get_width() < x2 + other.get_width()):
            if (y1 > y2 and y1 < y2 + other.get_height()) or (y1+this.get_height() < y2 + other.get_height() and y1+this.get_height() > y2):
                return True


    
