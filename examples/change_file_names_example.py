import os

os.chdir("C:\\Users\\ze179\\Videos\\to watch\\Jojo Part I")
ep_counter = 1
for file in os.listdir("."):
	new_name = f"JoJo's Bizarre Adventure - Phantom Blood - Episode {str(ep_counter)}.mkv"
	os.rename(file, new_name)
	ep_counter += 1


os.chdir("C:\\Users\\ze179\\Videos\\to watch\\Jojo Part II")
ep_counter = 1
for file in os.listdir("."):
	new_name = f"JoJo's Bizarre Adventure - Battle Tendency - Episode {str(ep_counter)}.mkv"
	os.rename(file, new_name)
	ep_counter += 1


os.chdir("C:\\Users\\ze179\\Videos\\to watch\\Jojo Part III")
ep_counter = 1
for file in os.listdir("."):
	new_name = f"JoJo's Bizarre Adventure - Stardust Crusaders - Episode {str(ep_counter)}.mkv"
	os.rename(file, new_name)
	ep_counter += 1


os.chdir("C:\\Users\\ze179\\Videos\\to watch\\Jojo Part IV")
ep_counter = 1
for file in os.listdir("."):
	new_name = f"JoJo's Bizarre Adventure - Diamond is Unbreakable - Episode {str(ep_counter)}.mkv"
	os.rename(file, new_name)
	ep_counter += 1


os.chdir("C:\\Users\\ze179\\Videos\\to watch\\Jojo Part V")
ep_counter = 1
for file in os.listdir("."):
	new_name = f"JoJo's Bizarre Adventure - Vento Aureo - Episode {str(ep_counter)}.mkv"
	os.rename(file, new_name)
	ep_counter += 1