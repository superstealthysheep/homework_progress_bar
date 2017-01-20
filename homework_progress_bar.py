#ask user for number of problems
#ask user for number of problems done so far
    #if problems done > 0, ask how long it took to get there
#calculate percentage done
#display progress bar with percentage

import sys
import readchar

def list_element_replace(target_list, target, replacement): #replaces target_list's target with replacement
    target_index = target_list.index(target)
    target_list.remove(target)
    target_list.insert(target_index, replacement)

def recalculate_values():    
    global percentage_done
    global progress_bar
    
    #finds percentage done
    percentage_done = problems_done / problem_count * 100
    
    #print("Percentage done: {}".format(percentage_done))
    
    #sets progress bar 
    progress_bar = "#" * int(percentage_done * (progress_bar_length) / 100) + "-" * int((100 - percentage_done) * (progress_bar_length) / 100)
        
    #print("Progress bar: {}".format(progress_bar))    

                                                                                        
def run():    
    global problem_count
    global problems_done
    global starting_time
    global progress_bar_length
    global time_unit_list
    global time_unit_name_list
    
    problem_count = 1
    problems_done = 0
    progress_bar_length = 30
    
    #finds number of problems
    while True:
        print("How many problems do you need to do? ")
        new_input = input("> ")
        
        #tries to assign input to int
        try:
            problem_count = int(new_input)
        
        #if input can't be made an int, make user try again
        except ValueError:
            print("Wait, that isn't a integer greater than zero. How can you have \"{}\" problems? ".format(new_input))
            continue
        
        #if problem count is lower than one, make user try again    
        if problem_count <= 0:
            print("It seems like you have a number of problems lower than one. Try again. ")
            continue
            
        #breaks loop if everything little thing gonna be alright
        break
        
    while True:    
        print("How many of those {} problem(s) have you done already? ".format(problem_count))
        new_input = input("> ")
        
        try:
            problems_done = int(new_input)
        
        except ValueError:
            print("Hmm... That isn't a nonnegative integer. How can you have \"{}\" problems done? ".format(new_input))
            continue
            
        if problems_done < 0:
            print("Really? It's impossible to have a negative number of problems done! ")
            continue
            
        if problems_done > problem_count:
            print("It looks like you told me you have more problems done than how many you had to begin with. Try again. ")
            continue
        
        #breaks out of loop if nothing is wrong with the input    
        break
        
    #defines all of the calculated values to prevent errors
    recalculate_values()   
        
    while percentage_done < 100:
        recalculate_values() 
        
        #sets next output
        next_output = "\r[{}] {}% done. ".format(progress_bar, round(percentage_done, 3))
        #clears output
        #sys.stdout.write(" " * (len(next_output) + 5))
        #sends out next output
        sys.stdout.write(next_output)
        
        #takes input and acts on it
        new_input = readchar.readkey()
                                                                                        
        if new_input == "+":
            problems_done = problems_done + 1
        elif new_input == "-":
            if problems_done > 0:
                problems_done = problems_done - 1
        elif new_input == "q":
            print("\nGoodbye.")
            exit()
              
run()    
