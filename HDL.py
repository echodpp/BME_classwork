def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice == "9":
            return


def input_HDL():
    HDL_input = input("Enter HDL value: ")
    return int(HDL_input)


def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL_result < 60:
        return "Borderline Low"
    else:
        return "Low"


def HDL_driver():
    HDL_value = input_HDL()
    HDL_result = check_HDL(HDL_value)
    output_HDL(HDL_value, HDL_result)


def output_HDL(HDL_value, HDL_result):
    print("The HDL value of {} is considered {}".format(HDL_value, HDL_result))


# Modify interface to add the HDL analysis option and call your HDL driver function
