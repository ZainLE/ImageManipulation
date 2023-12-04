import pygame

# initialize pygame and screen
pygame.init()
screen = pygame.display.set_mode((1200, 400))

red_input=float(input("Write the value of red between (0,255):  "))
green_input=float(input("Write the value of green between (0,255):  "))
blue_input=float(input("Write the value of blue between (0,255):  "))

class Filter():
    def __init__(self,image_file):
        self.image_file = image_file
        self.img = None
        self.arr = None
        
    def load_image(self):
        self.img = pygame.image.load(self.image_file).convert_alpha()
        self.arr = pygame.surfarray.array3d(self.img)
        # print(self.arr.shape)
        # print(self.arr)
            
    def save_image(self, path):
        surface = pygame.surfarray.make_surface(self.arr) # convert array back to pygame surface
        pygame.image.save(surface, path) # save the surface as png
        
class GrayScaleTransformer(Filter):
    def __init__(self, image_file):
        super().__init__(image_file)
        
    def transform(self):
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[1]):
                r,g,b = self.arr[i][j]
                avg = r/3 + g/3 + b/3
                self.arr[i,j] = [avg,avg,avg]

class MyFunnyFilter(Filter):
    def __init__(self, image_file):
        super().__init__(image_file)
        
    def transform(self):
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[1]):
                r,g,b = self.arr[i][j]
                self.arr[i][j]=[g,b,r]

class MyblackFilter(Filter):
    def __init__(self, image_file):
        super().__init__(image_file)
    
    def transform(self):
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[1]):
                self.arr[i][j]  =[0,0,0]



class MyWhiteFilter(Filter):
    def __init__(self, image_file):
        super().__init__(image_file)
    
    def transform(self):
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[1]):
                self.arr[i][j]  =[255,255,255]
                
                
                
class User_Filter(Filter):
    def __init__(self, image_file):
        super().__init__(image_file)
    
    def transform(self):
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[1]):
                self.arr[i][j]  =[red_input,green_input,blue_input]



    

image_file = "data/test_cut.png"
# image_file2= "data/test_gray.png"
# image_file3= "data/test_black.png"
# image_file4= "data/test_white.png"
# image_file5= "data/test_input.png"

#Gray 
transformer = GrayScaleTransformer(image_file)
transformer.load_image()
transformer.transform()
transformer.save_image("data/test_gray.png")

#Funny
transformer = MyFunnyFilter(image_file)
transformer.load_image()
transformer.transform()
transformer.save_image("data/test_funny.png")


# Black 
transformer = MyblackFilter(image_file)
transformer.load_image()
transformer.transform()
transformer.save_image("data/test_black.png")


#White 
transformer = MyWhiteFilter(image_file)
transformer.load_image()
transformer.transform()
transformer.save_image("data/test_white.png")


# User Input
transformer = User_Filter(image_file)
transformer.load_image()
transformer.transform()
transformer.save_image("data/test_input.png")



