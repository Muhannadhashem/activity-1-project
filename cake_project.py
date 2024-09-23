from turtle import Turtle, Screen
from project_functions import table, cake_maker, cake_decorations

# Initialize screen and turtle objects
sc = Screen()
turta = Turtle()

# Get user inputs for table dimensions and colors
width = int(input("Enter the width (100-200) for the table: "))  
height = int(input("Enter the height (0-100) for the table: "))  
table_color = input("Enter a color for the table: ")  
layer1_color = input("Enter a color for the first layer of cake: ")  
layer2_color = input("Enter a color for the second layer of cake: ")  
layer3_color = input("Enter a color for the third layer of cake: ")  

# Draw the table using the user inputs
table(width, height, table_color, turta)

# Draw the cake with the specified layers and colors
cake_maker(width, layer1_color, layer2_color, layer3_color, turta)

# Add decorations like a cherry or circle on top of the cake
cake_decorations(width, turta)

# Inform the user that the cake is being drawn
print("Your cake is loading! Happy Birthday!")
print("Press any key to exit......")

# Close the turtle screen when clicked
sc.exitonclick()
