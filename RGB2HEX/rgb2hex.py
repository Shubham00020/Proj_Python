"""
RGB to hex converter
"""
invalid_msg = "You entered a wrong value"
def rgb_hex():
  red = int(raw_input("R: "))
  if red < 0 or red > 255:
    print invalid_msg
    return
  green = int(raw_input("G: "))
  if green < 0 or green > 255:
    print invalid_msg
    return
  blue = int(raw_input("B: "))
  if blue < 0 or blue > 255:
    print invalid_msg
    return
  val = (red << 16) + (green << 8) + blue
  print (hex(val)[2:]).upper()

def hex_rgb():
  hex_val = raw_input("HEX: ")
  if len(hex_val) != 6:
    print invalid_msg
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "rgb(%s, %s, %s)" % (red, green, blue)

def convert():
  while True:
    option = raw_input("Enter 1 to conver RGB to HEX. \nEnter 2 to convert HEX to RGB. \nEnter X to Exit \n\t:")
    if option == '1':
      print "RGB to HEX . . ."
      rgb_hex()
    elif option == '2':
      print "HEX to RGB . . ."
      hex_rgb()
    elif option == 'X' or option == 'x':
      break
    else:
      print "Error."

convert()