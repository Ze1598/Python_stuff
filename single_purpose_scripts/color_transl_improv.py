# color translator eng-port

color_dict = {
    "blue": "azul",
    "red": "vermelho",
    "green": "verde",
    "yellow": "amarelo",
    "white": "branco",
    "black": "preto"
}


print(u"Welcome to my color translator, where you can translate some colour to portuguese. The available colors are blue, red, green, yellow, white and black.")

color_pick = str(input(u"Please choose one of the colors above:"))

for item in color_dict:
    if color_pick.lower() in color_dict:
        print("The color you chose translates as", color_dict[color_pick.lower()])
        break
    else:
        while color_pick.lower() not in color_dict:
            color_pick_2 = str(input(u"The color you chose is not valid. Please choose one of the colors above:"))
            if color_pick_2.lower() in color_dict:
                print("The color you chose translates as", color_dict[color_pick_2.lower()])
                break
        break


    
