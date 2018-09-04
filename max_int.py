# - Ef inputtið er ekki mínustala þá keyrir while lykkjan
# - Breytan max_int byrjar í 0 en verður alltaf jafnt og hæsta
#   sem notandi slær inn
# - Þegar mínustala er slegin inn þá prentar forritið út
#   max_int sem er þá hæsta talan sem að notandinn sló inn

max_int = 0
num_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    # Fill in the missing code
    if num_int > max_int: 
        max_int = num_int 
    
print("The maximum is", max_int)    # Do not change this line    
    



