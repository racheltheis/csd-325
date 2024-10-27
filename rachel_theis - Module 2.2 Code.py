#Rachel Theis
#CSD 325
#10.27.24

#This assignment was previously used in CSD 205. The purpose of the program is to gather first, middle, and last initials from user input. 

def user_initials():
    name_string = input("Enter your first, middle, and last name: ')
    #Error before the breakpoint 
    name_list = name_string.split()
    breakpoint()
    try:
        if len(name_list)==3:
            initials = name_list[0][:1] + name_list[1][:1] + name_list[2][:1]
            return initials 
        else:
            print('Error. Please enter exactly three names, separated by spaces.')
            return None
    except IndexError:
        print('Error. Please enter exactly three names, separated by spaces.')
        return Non
        #error after breakpoint
        


def main():
    initials = user_initials()
    if initials:
        print('Your initials are:', initials)

if __name__ == '__main__':
    main()

    
