# Function to draw the table
def table(width, height, table_color, turta):
   # Draw the rectangular top of the table
    turta.pensize("2")
    turta.begin_fill()
    turta.fillcolor(table_color)
    turta.fd(width)  # Move forward to create the top width of the table
    turta.left(90)
    turta.fd(height*0.3)  # Adjust height for the top part of the table
    turta.left(90)
    turta.fd(width)  # Complete the rectangle
    turta.left(90)
    turta.fd(height*0.3)
    turta.end_fill()

    # Draw the left long leg of the table
    turta.begin_fill()
    turta.fillcolor(table_color)
    turta.fd(height)  # Adjust for leg height
    turta.left(90)
    turta.fd(width*0.1)  # Width for the leg
    turta.left(90)
    turta.fd(height)  # Back up to the top of the leg
    turta.end_fill()

    # Draw the left short leg of the table
    turta.begin_fill()
    turta.fillcolor(table_color)
    turta.right(90)
    turta.fd(width*0.1)  # Move to position for the next leg
    turta.right(90)
    turta.fd(height*0.8)  # Shorter leg height
    turta.left(90)
    turta.fd(width*0.1)
    turta.left(90)
    turta.fd(height*0.8)
    turta.end_fill()

    # Draw the right short leg of the table
    turta.begin_fill()
    turta.fillcolor(table_color)
    turta.right(90)
    turta.fd(width*0.4)  # Move to the right side of the table
    turta.right(90)
    turta.fd(height*0.8)  # Shorter leg height
    turta.left(90)
    turta.fd(width*0.1)
    turta.left(90)
    turta.fd(height*0.8)
    turta.end_fill()

    # Draw the right long leg of the table
    turta.begin_fill()
    turta.fillcolor(table_color)
    turta.right(90)
    turta.fd(width*0.1)  # Move into position
    turta.right(90)
    turta.fd(height)  # Adjust for long leg height
    turta.left(90)
    turta.fd(width*0.1)
    turta.left(90)
    turta.fd(height)
    turta.end_fill()

    # Adjust position for cake drawing
    turta.up()
    turta.fd(width*0.1)
    turta.left(90)
    turta.fd(width*0.2)
    turta.right(90)
    turta.down()

# Function to draw the cake layers
def cake_maker(width, layer1_color, layer2_color, layer3_color, turta):
    # Draw the first layer of the cake
    turta.begin_fill()
    turta.fillcolor(layer1_color)
    turta.fd(30)  # Height of the first layer
    turta.left(90)
    turta.fd(width*0.6)  # Adjust layer width
    turta.left(90)
    turta.fd(30)  # Complete the layer
    turta.end_fill()

    # Draw the plate below the first layer
    turta.pensize("5")
    turta.pencolor("white")
    turta.left(90)
    turta.fd(width*0.6)  # Adjust plate width
    turta.left(90)
    turta.pensize("2")
    turta.pencolor("black")
    turta.fd(30)  # Back to starting point

    # Draw the second layer of the cake
    turta.begin_fill()
    turta.fillcolor(layer2_color)
    turta.left(90)
    turta.fd(width*0.1)  # Adjust height for the second layer
    turta.right(90)
    turta.fd(30)  # Second layer thickness
    turta.left(90)
    turta.fd(width*0.4)  # Adjust layer width
    turta.left(90)
    turta.fd(30)
    turta.end_fill()

    # Move position for the third layer
    turta.bk(30)
    turta.left(90)
    turta.fd(width*0.1)

    # Draw the third layer of the cake
    turta.begin_fill()
    turta.fillcolor(layer3_color)
    turta.left(90)
    turta.fd(30)  # Thickness of third layer
    turta.right(90)
    turta.fd(width*0.2)  # Width for third layer
    turta.right(90)
    turta.fd(30)  # Complete the layer
    turta.end_fill()

# Function to add decorations like a cherry or candle
def cake_decorations(width, turta):
    # Draw a circle on top (e.g., a cherry)
    turta.bk(30)
    turta.right(90)
    turta.fd(width*0.05)  # Position for cherry
    turta.left(180)
    turta.begin_fill()
    turta.fillcolor("light blue")
    turta.circle(width*0.05)  # Circle size based on width
    turta.end_fill()
    turta.bk(width*0.15)  # Move backward slightly

    # Draw a candle
    turta.begin_fill()
    turta.fillcolor("red")
    turta.fd(width*0.025)  # Candle thickness
    turta.left(90)
    turta.fd(35)  # Candle height
    turta.right(90)
    turta.fd(width*0.025)  # Complete candle
    turta.right(90)
    turta.fd(35)
    turta.end_fill()

    
    # This can be removed or modified according to project needs.
    turta.begin_fill()
    turta.fillcolor("white")
    turta.right(90)
    turta.fd(width*0.05)
    turta.left(90)
    turta.circle(10, 180)  # Frosting effect around cake
    turta.left(180)
    turta.circle(10, 180)
    turta.end_fill()
