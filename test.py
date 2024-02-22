#all code written by [insert pseudonym here] unless stated otherwise
import math
def get_average(lst, ind):
    counts = [["¬", -100]]
    for j in lst:
        found = False
        for i in counts:
                    
            if j[ind] in i[0] or i[0] in j[ind]:
                i[1] = i[1]+1
                found = True
        if found == False:
            counts.append([j[ind],1])
    
    max = [0,0]
    for i in counts:
        if i[1] > max[1]:
            max = i
    return max
    
def check_input(string, spec):
    a = input(string)
    if a == None:
        print("Please try again.")
        a = check_input(string, spec)
    if spec == 1:
        try:
            a = int(a)
            print(f"Data type of input is {type(a)} when str expected.\nTry again.")
            a = check_input(string, spec)
        except:
            pass
    elif spec[0] == 0:

        try:
            a = int(a)
        except:
            print(f"Data type of input is {type(a)} when int expected.\nTry again.")
            a = check_input(string, spec)
        
        if a < spec[1][0] or a > spec[1][1]:
            print(f"Error: input not within range of {spec[1][0]}-{spec[1][1]}.")
            a = check_input(string, spec)
    return a

gens = ("II", "III", "IV")

def Spartan(fireteam):
    name = check_input("\nInput name of Spartan: ", 1)
    tag = input("Input tag(numbers and letters only): ")
    generation = check_input("Input generation of Spartan(2-4): ", (0,(2,4)))
    color = check_input("Input armor color of Spartan: ", 1)
    weapon = check_input("Spartan's weapon of choice: ", 1)
    return (name, tag, gens[generation-2], color, weapon, fireteam)

all = []
print("Welcome to Halo Fireteam Generator.\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠋⠁⢀⡟⢿⠛⠛⠛⠋⠉⠉⠉⠛⢻⠛⡆⠀⠉⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢎⣥⡖⠀⢀⣀⣼⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢳⣀⡀⠀⠰⡦⡙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠋⠉⠁⢀⡏⠳⣾⠀⠀⠀⠀⠀⠀⠤⠀⢾⠖⠙⡆⠈⠉⠉⠻⣿⣾⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡼⠼⠓⠒⠂⠀⠀⣿⣆⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⣠⡟⠀⠀⠒⠒⠚⠧⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢠⠞⠉⠀⠀⠀⠀⠀⠀⠀⢸⠀⠹⡧⣤⣤⣤⣤⣤⣤⣤⣤⡤⡟⠁⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢸⠀⣀⣤⣴⠶⠶⠛⠛⠛⠯⢽⡾⠿⠿⢿⣿⣿⣿⣿⣿⢿⣿⣷⠾⠿⠛⠛⠻⠶⠶⣦⣤⣀⠀⢳⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀ ⠀⠀⠀⣸⠾⠿⣥⣤⠤⠔⠒⠒⠂⠈⠉⠉⢉⠉⡀⠈⠉⠉⠉⠉⢉⣉⣉⠉⡀⠐⠒⠒⠲⠦⢤⣬⠿⠽⢾⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢰⡇⠀⡰⠋⣀⣤⠄⠒⠒⠊⢉⡩⠥⠀⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢍⡉⠁⠒⠒⠢⢤⣀⡉⢢⢀⣈⡇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢹⠛⣷⣿⠁⠱⢄⠀⢀⠔⠉⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠈⠲⢄⠀⣀⠼⠁⢹⣿⡟⣿⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢸⠀⣿⣧⠀⠀⠀⠈⠁⠀⠀⡠⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢦⡀⠀⠀⠉⠀⠀⠀⢸⣿⠀⣿⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢸⠀⣿⣿⠀⠀⠀⢀⡤⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠒⠤⡀⠀⠀⠀⣌⣿⠀⣻⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣼⣀⣿⣯⣇⠀⠀⠘⣆⠀⠀⠀⠀do whatever.  ⢀⠇⠀⠀⢠⣿⣿⣀⣸⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⣠⣾⣿⣯⣿⠻⡝⢦⡀⠀⠈⠑⢤⣀⣀⣀⡴⠀⠀⠀⠀⠀⠀⢢⣀⣀⣀⣠⠔⠁⠀⠀⣰⢿⠟⢻⣩⣿⣿⡄⠀⠀⠀⠀⠀\n⣖⣶⣾⣿⣿⣿⣿⣿⡟⣧⠀⠈⠲⣝⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢞⡷⠁⠀⢸⡿⣾⣿⣭⣿⣿⣷⣶⣶\n⡟⣉⣉⡁⢸⣿⣿⣿⣹⡿⣄⠀⠀⠈⠢⣉⠲⢄⡀⠀⢀⠔⢋⣉⣉⣉⣉⣉⠲⣄⠀⢀⣠⠖⢋⠴⠋⠀⠀⢠⡿⣿⣽⣿⣿⣿⣋⣉⣙⣿\n⣩⣿⣿⣿⣿⣛⣿⢿⣦⣀⣿⡧⣄⠀⠀⠈⠙⠒⠬⣙⣳⣶⣟⣾⣷⣲⣿⣿⣷⣞⣋⠩⠔⠊⠁⠀⠀⢀⠴⣿⣄⣠⡿⢿⣟⣿⣿⣿⣿⣽\n⡿⠏⠁⠀⠀⠀⠀⠀⣘⣿⣿⣿⣮⡳⡄⠀⠀⠀⠀⠀⠈⠙⣿⠉⠉⠉⠉⢹⡏⠁⠀⠀⠀⠀⠀⢀⢔⣡⣾⣿⣿⣏⠀⠀⠀⠀⠀⠀⠉⠿\n⣁⣀⣠⣤⣴⣾⣿⡉⠀⣿⠙⢿⣿⣽⣟⠄⠀⠀⠀⠀⣠⣴⣿⣄⣀⣀⣀⣸⣧⣄⠀⠀⠀⠀⠀⢿⣿⣿⣿⠟⡿⠈⠉⣷⣶⣦⣤⣄⣀⣀\n⢉⣿⣿⣟⣿⣿⣿⣷⡀⠘⡄⠀⢻⡿⣟⠀⠀⠀⣠⠞⠁⡏⠉⠉⠉⠉⠉⠉⢹⠇⠑⢄⠀⠀⠀⣨⣿⡟⠁⠀⡗⢀⣴⣿⣿⣿⣿⣿⣾⣿\n⡸⢿⣿⣿⣀⣤⣿⣟⣻⠄⠃⠀⢸⡇⠉⠻⢿⣏⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⣩⣴⠟⠋⠀⡇⠀⣸⠁⢾⡛⠻⠥⣀⣽⣿⡿⢻\n⠑⣤⣉⠤⠜⠛⠉⠁⠀⠀⠘⡄⢸⡇⠀⣤⠾⠋⠑⢄⠀⢣⠀⠀⠀⠀⠀⠀⢸⠀⣠⠞⠙⠻⣦⡀⢨⡇⢠⠃⠀⠀⠀⠉⠒⠢⠤⣉⣧⣾\n⣼⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⡧⣤⡟⠀⠀⠀⠀⠑⣾⡷⠶⠶⠶⠶⣶⣿⡋⠁⠀⠀⠀⢹⣇⡼⣿⠯⠤⠤⠤⣤⣤⣤⢤⣤⣬⣭⣿\n⠈⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠳⣄⣿⡐⣦⣤⣀⣼⡟⠀⠀⠀⠀⠀⠀⠹⣷⢀⣠⣴⢲⣿⣯⠖⠁⠀⠀⠀⠀⣸⣟⣿⠀⣟⢛⣃⢹")
print("Input the roster for a team of Spartan super-soldiers, including \ntheir: \n- name\n- tag(numbers and letters)\n- generation(2-4)\n- armor color\n- weaponry")
for i in range(check_input("How many teams would you like to input? ", (0, (-math.inf, math.inf)))):
    team = [[],[]]
    name = check_input("Name of Fireteam: ", 1)
    team[0] = name
    for i in range(int(check_input(f"How many Spartans are in {team[0]} Team? ",(0, (-math.inf, math.inf))))):
        team[1].append(Spartan(name))
    all.append(team)

for i in all:
    
    print(f"\nRoster for {i[0]} Team:")
    for j in i[1]:
        print(f"{j[0]}-{j[1]} is a Spartan-{j[2]}. Their armor color is {j[3]} and they carry a {j[4]}.")

    if get_average(i[1], 2)[1] == 1:
        print(f"No spartans in {i[0]} Team share generations.")
    else:
        print(f"\nMost common generation for spartans in {i[0]} Team is {get_average(i[1], 2)[0]}\n{get_average(i[1], 2)[1]} Spartans have it.")
    
    if get_average(i[1], 3)[1] == 1:
        print(f"No spartans in {i[0]} Team share armor colors.")
    else:
        print(f"\nMost common armor color for {i[0]} Team is {get_average(i[1], 3)[0]}\n{get_average(i[1], 3)[1]} Spartans have it.")
    
    if get_average(i[1], 4)[1] == 1:
        print(f"No spartans in {i[0]} Team share common weapons.")
    else:
        print(f"\nMost common weapon of choice in {i[0]} Team is {get_average(i[1], 4)[0]}\n{get_average(i[1], 4)[1]} Spartans have it.")