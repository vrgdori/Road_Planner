import time
from map import GridMap
from algorithm import plan_path
import random

r=random.randint(1, 10)

def print_grid(grid_map, current_pos, path, target):
    """A rács kirajzolása"""
    print("\n" + "=" * 25)
    for y in range(grid_map.height):
        row_str = ""
        for x in range(grid_map.width):
            pos = (x, y)
            if pos == current_pos:
                row_str += " A "  # Drón
            elif pos == target:
                row_str += " T "  # Cél
            elif pos in grid_map.obstacles:
                row_str += " X "  # Akadály
            elif path and pos in path:
                row_str += " o "  # Kiszámolt útvonal
            else:
                row_str += " . "  # Üres mező
        print(row_str)
    print("=" * 25)

def main():
    grid_height = int(input("Kérlek, add meg a pálya magasságát: "))
    grid_width = int(input("Kérlek, add meg a pálya szélességét: "))
    grid = GridMap(grid_height,grid_width)
    current_pos = (0,0)
    goal_pos = (grid_height-1,grid_width-1)
    
    current_path = plan_path(grid, current_pos, goal_pos)
    r=random.randint(1, len(current_path))

    print(f"Kezdeti útvonal kiszámítva ({len(current_path)} lépés): {current_path}")
    print_grid(grid, current_pos, current_path, goal_pos)

    step = 0
    for pos in current_path:
        step += 1
        current_pos = pos
        print(f"\nLépés {step}: Jelenlegi pozíció: {current_pos}")
        
        if step == r :
            dynamic_obstacle = current_path[step + 1]  
            print(f"\nÚj akadály észlelve a pályán: {dynamic_obstacle}!")
            
            grid.add_obstacle(dynamic_obstacle)
            
            print("Útvonal újratervezése...")
            new_path = plan_path(grid, current_pos, goal_pos)
            
            if new_path and step<len(current_path):
                print(f"Sikeres újratervezés! Új útvonal: {new_path}")
                print_grid(grid, current_pos, new_path, goal_pos)
                r=r+random.randint(1, 5)
                if r>= (len(current_path)-5):
                    break
            else:
                print("HIBA: Nincs lehetséges útvonal a célhoz!")
                break
        
        time.sleep(0.5)

if __name__ == "__main__":
    main()