import sys 




def main(argv):
    output_string = ""
    striped_input_string = ""
    pretty_string = ""
    units_to_shift = int(sys.argv[1])
    #print(units_to_shift)
    line = sys.stdin.readline() 
    line = line.upper()
    line = line.replace(" ", "")
    #print(line)
    for sym in line:
      if sym.isalpha():
        striped_input_string += sym
    for symbol in striped_input_string:
      ascii_char = ord(symbol)
      if(ascii_char + units_to_shift > 90):
        #print('OVERSHIFT FOUND')
        over_shift = (ascii_char + units_to_shift) - 90
        while over_shift > 26:
          over_shift -= 26
        over_shift += -1
        #print('Overshifted by: ', over_shift)
        output_string += chr(ord('a') + over_shift).upper()
        continue
      output_string += chr(ascii_char + units_to_shift).upper()
    #print(output_string)
    idx = 0
    for i in output_string:
      pretty_string += i
      if idx == 4:
        pretty_string+= " "
        idx = 0
        continue
      idx += 1
    print(pretty_string)
    #print(sys.stdout)

if __name__ == "__main__": 
    main(sys.argv)
