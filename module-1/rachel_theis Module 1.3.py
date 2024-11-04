#Rachel Theis
#CSD 325
#10.27.24

#This program will loop through a song, decreasing the number in the song by 1, using a user inputted number until the number is 0.

while True:
    try:
        bottles_of_beer = int(input('Please choose a number between 1 and 99.\nHow many bottles of beer are on the wall?: '))
        
        if bottles_of_beer < 1 or bottles_of_beer >99:
            print ('Error. Please enter a number between 1 and 99')
            continue
        
        while bottles_of_beer > 0:
            if bottles_of_beer > 1:
                print(bottles_of_beer, 'bottles of beer on the wall', bottles_of_beer, 'bottles of beer.')
            
            else:
                print (bottles_of_beer, 'bottle of beer on the wall', bottles_of_beer, 'bottle of beer.')
            
            
            bottles_of_beer -= 1
            
            if bottles_of_beer >0 :
                print ('Take one down, pass it around', bottles_of_beer, 'bottle(s) of beer on the wall.')
            else:
                print('Take one down, pass it around, 0 bottles of beer on the wall. \nTime to buy more beer!')
                
        break
    
    except ValueError:
        print('Error, please try again with a whole number between 1 and 99.')
    
#References
#Pankaj. (2024). Python ValueError Exception Handling Examples. Digitalocean.com. https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples#1-what-is-python-valueerror
#solo learn. (2022). How to use while loop for exception handling? | Sololearn: Learn to code for FREE! Sololearn.com. https://www.sololearn.com/en/Discuss/2958647/how-to-use-while-loop-for-exception-handling