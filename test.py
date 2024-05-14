#all_teams code written by AN unless stated otherwise
import math
gens = ("II", "III", "IV")
def get_average(member_list, trait):
    counter = {

    }
    if(trait == "gen"):
        for member in member_list:
            if member.generation in counter:
                counter[member.generation] += 1
            else:
                counter[member.generation] = 1
    elif(trait == "color"):
        for member in member_list:
            if member.color in counter:
                counter[member.color] += 1
            else:
                counter[member.color] = 1
    #assume weapon
    else:
        for member in member_list:
            if member.weapon in counter:
                counter[member.weapon] += 1
            else:
                counter[member.weapon] = 1
        
    max_key = ""
    for key in counter:
        if(max_key == ""):
            max_key = key
        elif(counter[key] > counter[max_key]):
            max_key = key
    return [max_key, counter[max_key]]

    
def check_input(string, spec):
    a = input(string)
    if a == "":
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


def make_spartan():
    name = check_input("\nInput name of Spartan: ", 1)
    tag = input("Input tag(numbers and letters only): ")
    generation = check_input("Input generation of Spartan(2-4): ", (0,(2,4)))
    color = check_input("Input armor color of Spartan: ", 1)
    weapon = check_input("Spartan's weapon of choice: ", 1)
    return Spartan(name, tag, gens[generation-2], color, weapon)
class Spartan():
    def __init__(self, name, tag, generation, color, weapon) -> None:
        self.name = name
        self.tag = tag
        self.generation = generation
        self.color = color
        self.weapon = weapon
class Team():
    def __init__(self, name, members) -> None:
        self.name = name
        self.members = members

all_teams = []
print("Welcome to Halo Fireteam Generator.")
#next line prints out ASCII art. Cut off in PDF, but it's nothing important to functionality.
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠋⠁⢀⡟⢿⠛⠛⠛⠋⠉⠉⠉⠛⢻⠛⡆⠀⠉⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢎⣥⡖⠀⢀⣀⣼⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢳⣀⡀⠀⠰⡦⡙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠋⠉⠁⢀⡏⠳⣾⠀⠀⠀⠀⠀⠀⠤⠀⢾⠖⠙⡆⠈⠉⠉⠻⣿⣾⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡼⠼⠓⠒⠂⠀⠀⣿⣆⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⣠⡟⠀⠀⠒⠒⠚⠧⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢠⠞⠉⠀⠀⠀⠀⠀⠀⠀⢸⠀⠹⡧⣤⣤⣤⣤⣤⣤⣤⣤⡤⡟⠁⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢸⠀⣀⣤⣴⠶⠶⠛⠛⠛⠯⢽⡾⠿⠿⢿⣿⣿⣿⣿⣿⢿⣿⣷⠾⠿⠛⠛⠻⠶⠶⣦⣤⣀⠀⢳⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀ ⠀⠀⠀⣸⠾⠿⣥⣤⠤⠔⠒⠒⠂⠈⠉⠉⢉⠉⡀⠈⠉⠉⠉⠉⢉⣉⣉⠉⡀⠐⠒⠒⠲⠦⢤⣬⠿⠽⢾⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢰⡇⠀⡰⠋⣀⣤⠄⠒⠒⠊⢉⡩⠥⠀⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢍⡉⠁⠒⠒⠢⢤⣀⡉⢢⢀⣈⡇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢹⠛⣷⣿⠁⠱⢄⠀⢀⠔⠉⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠈⠲⢄⠀⣀⠼⠁⢹⣿⡟⣿⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢸⠀⣿⣧⠀⠀⠀⠈⠁⠀⠀⡠⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢦⡀⠀⠀⠉⠀⠀⠀⢸⣿⠀⣿⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢸⠀⣿⣿⠀⠀⠀⢀⡤⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠒⠤⡀⠀⠀⠀⣌⣿⠀⣻⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣼⣀⣿⣯⣇⠀⠀⠘⣆⠀⠀it does stuff.  ⢀⠇⠀⠀⢠⣿⣿⣀⣸⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⣠⣾⣿⣯⣿⠻⡝⢦⡀⠀⠈⠑⢤⣀⣀⣀⡴⠀⠀⠀⠀⠀⠀⢢⣀⣀⣀⣠⠔⠁⠀⠀⣰⢿⠟⢻⣩⣿⣿⡄⠀⠀⠀⠀⠀\n⣖⣶⣾⣿⣿⣿⣿⣿⡟⣧⠀⠈⠲⣝⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢞⡷⠁⠀⢸⡿⣾⣿⣭⣿⣿⣷⣶⣶\n⡟⣉⣉⡁⢸⣿⣿⣿⣹⡿⣄⠀⠀⠈⠢⣉⠲⢄⡀⠀⢀⠔⢋⣉⣉⣉⣉⣉⠲⣄⠀⢀⣠⠖⢋⠴⠋⠀⠀⢠⡿⣿⣽⣿⣿⣿⣋⣉⣙⣿\n⣩⣿⣿⣿⣿⣛⣿⢿⣦⣀⣿⡧⣄⠀⠀⠈⠙⠒⠬⣙⣳⣶⣟⣾⣷⣲⣿⣿⣷⣞⣋⠩⠔⠊⠁⠀⠀⢀⠴⣿⣄⣠⡿⢿⣟⣿⣿⣿⣿⣽\n⡿⠏⠁⠀⠀⠀⠀⠀⣘⣿⣿⣿⣮⡳⡄⠀⠀⠀⠀⠀⠈⠙⣿⠉⠉⠉⠉⢹⡏⠁⠀⠀⠀⠀⠀⢀⢔⣡⣾⣿⣿⣏⠀⠀⠀⠀⠀⠀⠉⠿\n⣁⣀⣠⣤⣴⣾⣿⡉⠀⣿⠙⢿⣿⣽⣟⠄⠀⠀⠀⠀⣠⣴⣿⣄⣀⣀⣀⣸⣧⣄⠀⠀⠀⠀⠀⢿⣿⣿⣿⠟⡿⠈⠉⣷⣶⣦⣤⣄⣀⣀\n⢉⣿⣿⣟⣿⣿⣿⣷⡀⠘⡄⠀⢻⡿⣟⠀⠀⠀⣠⠞⠁⡏⠉⠉⠉⠉⠉⠉⢹⠇⠑⢄⠀⠀⠀⣨⣿⡟⠁⠀⡗⢀⣴⣿⣿⣿⣿⣿⣾⣿\n⡸⢿⣿⣿⣀⣤⣿⣟⣻⠄⠃⠀⢸⡇⠉⠻⢿⣏⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⣩⣴⠟⠋⠀⡇⠀⣸⠁⢾⡛⠻⠥⣀⣽⣿⡿⢻\n⠑⣤⣉⠤⠜⠛⠉⠁⠀⠀⠘⡄⢸⡇⠀⣤⠾⠋⠑⢄⠀⢣⠀⠀⠀⠀⠀⠀⢸⠀⣠⠞⠙⠻⣦⡀⢨⡇⢠⠃⠀⠀⠀⠉⠒⠢⠤⣉⣧⣾\n⣼⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⡧⣤⡟⠀⠀⠀⠀⠑⣾⡷⠶⠶⠶⠶⣶⣿⡋⠁⠀⠀⠀⢹⣇⡼⣿⠯⠤⠤⠤⣤⣤⣤⢤⣤⣬⣭⣿\n⠈⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠳⣄⣿⡐⣦⣤⣀⣼⡟⠀⠀⠀⠀⠀⠀⠹⣷⢀⣠⣴⢲⣿⣯⠖⠁⠀⠀⠀⠀⣸⣟⣿⠀⣟⢛⣃⢹")
print("Input the roster for a team of Spartan super-soldiers, including") 
print("their: \n- name\n- tag(numbers and letters)\n- generation(2-4)\n- armor color\n- weaponry")
num_teams = check_input("How many teams would you like to input? ", (0, (-math.inf, math.inf)))
for i in range(num_teams):
    team_name = check_input("Name of Fireteam: ", 1)
    members = []
    for i in range(check_input(f"How many Spartans are in {team_name} Team? ",(0, (-math.inf, math.inf)))):
        members.append(make_spartan())
    all_teams.append(Team(team_name, members))

for i in all_teams:
    
    print(f"\nRoster for {i.name} Team:")
    for member in i.members:
        print(f"{member.name}-{member.tag} is a Spartan-{member.generation}. Their armor color is {member.color} and they carry a {member.weapon}.")

    average_output = get_average(i.members, "gen")
    if average_output[1] == 1:
        print(f"\nNo spartans in {i.name} Team share generations.")
    else:
        print(f"\nMost common generation for spartans in {i.name} Team is {average_output[0]}\n{average_output[1]} Spartans have it.")
    
    average_output = get_average(i.members, "color")
    if average_output[1] == 1:
        print(f"\nNo spartans in {i.name} Team share armor colors.")
    else:
        print(f"\nMost common armor color for {i.name} Team is {average_output[0]}\n{average_output[1]} Spartans have it.")
    
    average_output = get_average(i.members, "weapon")
    if average_output[1] == 1:
        print(f"\nNo spartans in {i.name} Team share common weapons.")
    else:
        print(f"\nMost common weapon of choice in {i.name} Team is {average_output[0]}\n{average_output[1]} Spartans have it.")
