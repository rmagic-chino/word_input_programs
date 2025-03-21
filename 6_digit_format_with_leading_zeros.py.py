#define command
def main():

    #input number
    number = input("Enter number (0-1000): ")
    formatted_number = f"{int(number):06d}"
    print("Output: ", formatted_number)
    #print output

if __name__ == "__main__":
    main()
#execute
