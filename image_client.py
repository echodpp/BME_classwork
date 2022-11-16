from tkinter import filedialog, ttk, Tk, Label
import base64
import requests
from PIL import ImageTk, Image


# def main_window():
#     def button_click():
#         upload_image()
#         print("")

#     root = Tk()
#     root.title("Images")
#     ttk.Label(root, text="Upload Image").grid(row=0, column=0)


def upload_image():
    filename = get_image_filename()
    b64_string =convert_file_to_b64(filename)
    netid='xc184'
    id_no=10086
    upload_b64_to_server(b64_string,netid,id_no)

def get_image_filename():
    filename = filedialog.askopenfilename()
    return filename

def convert_file_to_b64(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string

def upload_b64_to_server(b64_string,netid,id_no):
    url = "http://vcm-21170.vm.duke.edu/add_image"
    data = {"image": b64_string, "net_id": netid, "id_no": id_no}
    r = requests.post(url, json=data)
    return print(r.text), print(r.status_code)

# if __name__ == "__main__":
#     upload_image()

    
def download_b64_from_server():
    url = "http://vcm-21170.vm.duke.edu/get_image/xc184/10086"
    r = requests.get(url)
    print(r.text)
    print(r.status_code)
    b64_string = r.text
    convert_b64_to_file(b64_string)

def convert_b64_to_file(b64_string):
    image_bytes = base64.b64decode(b64_string)
    filename = filedialog.asksaveasfilename()
    with open(filename, "wb") as out_file:
        out_file.write(image_bytes)

if __name__ == "__main__":
    download_b64_from_server()
