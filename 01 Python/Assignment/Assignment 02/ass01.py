
def analyze_list_number(user_list):
    #remove duplicate values
    update_list = list(dict.fromkeys(user_list))
    # print(update_list)

    list_dict = {
        'original list':user_list,
        'the unique values':update_list,
        'length of original list':len(user_list),
        'length of unique values list':len(update_list),
        
    }

    return list_dict

try:
    user_input = input("Enter numbers seperated by spaces: ").split()

    # print(user_input)
    user_list = list(map(int,user_input))
    # print(user_list)


    #funtion call here
    analyze_result = analyze_list_number(user_list)


    #print formated dictionry
    for key,value in analyze_result.items():
        print(f"{key}:{value}")

    # print(analyze_result)
    

except ValueError:
    print("Please enter only numbers.")