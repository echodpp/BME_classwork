def input_HDL():
    HDL_input = input("Enter HDL test result: ")
    test_info = HDL_input.split("=")
    if test_info[0] == "HDL":
        return int(test_info[1])


def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL_result < 60:
        return "Borderline Low"
    else:
        return "Low"
