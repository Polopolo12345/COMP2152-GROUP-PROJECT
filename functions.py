import os
import random

def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]
    print(" | !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print(" | You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print(" | You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print(" | You used " + first_item + " but it's not helpful")
    return belt, health_points

def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print(" | Your belt: ", belt)
    return loot_options, belt

# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
    print(ascii_image)
    print(" | Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print(" | You have killed the monster")
    else:
        # Player only damaged the monster
        m_health_points -= combat_strength
        print(" | You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points

# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print(" | Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print(" | Player is dead")
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print(" | The monster has reduced Player's health to: " + str(health_points))
    return health_points

# Recursion
# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    if num_dream_lvls == 1:
        print(" | You are in the deepest dream level now")
        print(" |", end=" ")
        input("Start to go back to real life? (Press Enter)")
        print(" | You start to regress back through your dreams to real life.")
        return 2
    else:
        return 1 + int(inception_dream(num_dream_lvls - 1))

def load_total_monsters_killed():
    """Loads the total number of monsters killed from the save file."""
    if not os.path.exists("save.txt"):
        return 0
    try:
        with open("save.txt", "r") as file:
            for line in file:
                if line.startswith("Total Monsters Killed:"):
                    return int(line.split(":")[-1].strip())
    except FileNotFoundError:
        return 0
    return 0

def save_game(winner, hero_name="", num_stars=0):
    total_monsters_killed = load_total_monsters_killed()
    with open("save.txt", "w") as file:
        if winner == "Hero":
            total_monsters_killed += 1
        file.write(f"Total Monsters Killed: {total_monsters_killed}\n")

def load_game():
    try:
        with open("save.txt", "r") as file:
            print(" | Loading from saved file ...")
            lines = file.readlines()
            for i in lines:
                print(i.strip())
            return lines
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return None

def adjust_combat_strength(combat_strength, m_combat_strength):
    last_game = load_game()
    if last_game:
        if "Hero" in last_game[0] and "gained" in last_game[0]:
            num_stars = int(last_game[0].split()[-2])
            if num_stars > 3:
                print(" | ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game[0]:
            combat_strength += 1
            print(" | ... Increasing the hero's combat strength since you lost last time")
        else:
            print(" | ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")

def display_shop(monsters_killed):
    from feature import shop_items

    print("Welcome to the Shop!")
    print(f"You have killed {monsters_killed} monsters.")
    
    items = shop_items(monsters_killed)
    
    if not items:
        print("No items are available for purchase.")
        return
    
    print("Available items:")
    for idx, item in enumerate(items, start=1):
        print(f"{idx}. {item['name']} ({item['type']}, {item['rarity']}) - {item['price']} gold")
    
    choice = input("Enter the number of the item you want to purchase (or 'exit' to leave): ")
    
    if choice.lower() == 'exit':
        print("Leaving the shop...")
        return
    
    try:
        choice_idx = int(choice) - 1
        if choice_idx < 0 or choice_idx >= len(items):
            print("Invalid choice. Try again.")
            return
        
        selected_item = items[choice_idx]
        print(f"You purchased {selected_item['name']}!")
        
        # Update hero's inventory (this would depend on your inventory system)
        # Example: hero_inventory.append(selected_item)
        
    except ValueError:
        print("Invalid input. Please enter a number.")