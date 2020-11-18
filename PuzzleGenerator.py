import random

def generate():
    puzzle = [1,2,3,4,5,6,7,0]
    random.shuffle(puzzle)
    file = open("Puzzles.txt", "a") 
    file.write(str(puzzle)+"\n")


for i in range(0,50):
    generate()
