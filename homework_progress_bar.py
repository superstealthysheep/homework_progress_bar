#ask user for number of problems
#ask user for number of problems done so far
    #if problems done > 0, ask how long it took to get there
#start timer (from how long it took to get there)
#calculate percentage done
#display progress bar with percentage and expected time

import sys
import time

def list_element_replace(target_list, target, replacement): #replaces target_list's target with replacement
    target_index = target_list.index(target)
    target_list.remove(target)
    target_list.insert(target_index, replacement)

def recalculate_values():    
    global percentage_done
    global progress_bar
    global even_nicer_time_remaining
    
    #finds percentage done
    percentage_done = problems_done / problem_count * 100
    
    #print("Percentage done: {}".format(percentage_done))
    
    #sets progress bar 
    progress_bar = "#" * int(percentage_done * (progress_bar_length) / 100) + "-" * int((100 - percentage_done) * (progress_bar_length) / 100)
    #sets problem_time_avg average time per problem
    try:
        problem_time_average = (time.time() - starting_time)/problems_done #time elapsed/problems done during that time
    except ZeroDivisionError:
        problem_time_average = 0
        
    #print("Progress bar: {}".format(progress_bar))    
        
    #sets predicted time remaining
    time_remaining = (problem_count - problems_done) * problem_time_average
    
    #print("Predicted time remaining: {} sec".format(time_remaining))
    
    
    #convert time_remaining back to string
    #initalizes list times_remaining with "seed"
    times_remaining = [int(time_remaining)]
    
    #print("times_remaining intialized: {}".format(times_remaining))
    
    for unit in reversed(time_unit_list):
        index = time_unit_list.index(unit)
        #print("index: {}".format(index))
        
        #sets previous_unit to the most recent addition to times_remaining
        previous_unit = times_remaining[0]
        
        #sets unit_conversion_factor
        #if the index is the last in the list, unit_conversion_factor is 1
        if index == len(time_unit_list) - 1:
            unit_conversion_factor = 1
        
        #if index == 0, there's no more converting to be done. Break!
        if index == 0:
            break
            
        else:
            unit_conversion_factor = time_unit_list[index - 1] / (time_unit_list[index])
            
        #if the number of a unit is greater than zero, 
        if int(previous_unit // unit_conversion_factor) > 0:
            
            #converts the previous unit to WHOLE current units
            current_unit = int(previous_unit // unit_conversion_factor)
            #sets the new_previous_unit to the remainder
            new_previous_unit = int(previous_unit % unit_conversion_factor)
            
            #puts new values into times_remaining
            
            list_element_replace(times_remaining, previous_unit, new_previous_unit)
            #puts the current_unit in front of the new_previous_unit
            times_remaining.insert(0, current_unit)
            
            #print("Times remaining: {}".format(times_remaining))
            #print("Unit conversion factor: {}".format(unit_conversion_factor))
            #print(time_unit_list[index])
            #print(time_unit_list[index - 1])
            
            
    
    
    #print("Times remaining: {}".format(times_remaining))
    
    #intitializes nice_times_remaining, times_remaining but with units.
    nice_times_remaining = []
    
    
    for element in reversed(times_remaining):
        index = (times_remaining.index(element) - len(times_remaining)) #takes the index and puts it into negative terms
        #makes the index-th term of times_remaining into a string and adds units, and then inserts that to the corresponding spot in nice_times_remaining
        nice_times_remaining.insert(index, str(times_remaining[index]) + " " + time_unit_name_list[index])
        index = index - 1
        

        
    #makes nice_times_remaining into even_nicer_time_remaining, a string fit for display
    even_nicer_time_remaining = ", ".join(nice_times_remaining)
    #even_nicer_time_remaining = str(times_remaining)
    #even_nicer_time_remaining = nice_times_remaining
    
    
    #In case the number of problems completed is zero, even_nicer_time_remaining = "?"
    if problems_done == 0:
        even_nicer_time_remaining = "? sec"
        
    #print("Even nicer time remaining: {}".format(even_nicer_time_remaining))

def run():    
    global problem_count
    global problems_done
    global starting_time
    global progress_bar_length
    global time_unit_list
    global time_unit_name_list
    
    problem_count = 1
    problems_done = 0
    time_used = 0
    time_unit_list = [86400, 3600, 60, 1] #days, hours, minutes, seconds (counted by seconds)
    time_unit_name_list = ["day(s)","hour(s)", "min(s)", "sec"]
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
        
    if problems_done > 0:
        while True:
            #asks for time_used
            print("How long have you spent doing those {} problem(s)? (hr:min:sec)".format(problems_done))
            new_input = input("> ")
            
            #splits the input along ":"'s and makes a list
            time_list = new_input.split(":")
            
            
            #initializes a variable that will switch to True if the below for loop fails.
            for_loop_failure = False
            #initalizes a variable that will hold the error message in case the aforementioned loop fails
            for_loop_error_message = ""
            
            #changes time_list from a list of strings to a list of ints
            for element in time_list:
                #records element's index as element_index
                element_index = time_list.index(element)
                
                #tries to assign element to an int, returns element_int
                try:
                    element_int = int(element)
                    
                #in case of ValueError, throws error
                except ValueError:
                    #sets failure var to True
                    for_loop_failure = True
                    #sets faliure message
                    for_loop_error_message = "You included a foreign character. "
                    break
                    
                #in case that time_list is longer than time_unit_list, throws error
                if len(time_list) > len(time_unit_list):
                    for_loop_failure = True
                    #sets failure message
                    for_loop_error_message = "You gave too many units for time. "
                    break
                    
                #removes element
                time_list.remove(element)
                #and puts element_int in its place
                time_list.insert(element_index, element_int)
            
            #in case for loop fails,
            if for_loop_failure:
                #make user try again
                print("Try again. {}".format(for_loop_error_message))
                continue
            
            #sets the index to start counting down the unit_list from
            time_unit_index = -1
            
            #takes time_list and converts it all to seconds (returns to time_used)
            for num_of_units in reversed(time_list):
                time_used = time_used + time_unit_list[time_unit_index] * num_of_units
                time_unit_index = time_unit_index - 1
            
            #breaks out of loop if everything looks good
            break
    
    #sets the starting time        
    starting_time = time.time() - time_used            
            

        
    
    #defines all of the calculated values to prevent errors
    recalculate_values()   
        
    while percentage_done < 100:
        recalculate_values() 
        
        #sets next output
        next_output = "\r[{}] {}% done; {} remaining ".format(progress_bar, percentage_done, even_nicer_time_remaining)
        #clears output
        #sys.stdout.write(" " * (len(next_output) + 5))
        #sends out next output
        sys.stdout.write(next_output)
        
        if new_input == "+":
            problems_done = problems_done + 1
        elif new_input == "-":
            if problems_done > 0:
                problems_done = problems_done - 1
        
        
        
        time.sleep(1)
        
        
        
        
        
        
run()    


#random_list = [1, 2, 3, 4, 5, 6]
#list_element_replace(random_list, 3, 9000)
#print("Success! Target replaced.")
#print(random_list)
        
        
        
        
        
        
        
        
        
        
    
