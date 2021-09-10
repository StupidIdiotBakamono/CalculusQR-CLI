import mandatum
import os
import qrcode
import cv2
import time
import rich

# options for menu
menu_options = ["Make QR-Code", "Read QR-Code", "Exit"]
# menu
menu = mandatum.Menu(
    options=menu_options,
    theme=["red", "blue", "yellow"],
    bold_text=True    
)

console = rich.console.Console()


# getting image path
def get_image_path(file):
    return os.path.join("QRs", file)    





# Make QR Class
class MakeQR():
    def __init__(self):
        self.name = "Make-QR"
        self.desciption = "Helps in making QR-Code"
        self.theme = ["red", "magenta"]

        # initializing makeqr mode
        self.mode = mandatum.Mode(
            name=self.name,
            description=self.desciption,
            theme=self.theme,
            bold_text=True
        )

        self.mode.init_prompt()
        
        self.prompt = self.mode.prompt
    
    # Making qr
    def make_qr(self):
        print()
        self.mode.print_details()

        text = self.prompt.input("\nText to make QR : ")
        time.sleep(.5)

        image_file = self.prompt.input("Image name for QR : ")
        time.sleep(.5)

        image_file = get_image_path(image_file)

        qr = qrcode.make(text)
        qr.save(image_file)

        alert = mandatum.Alert(color="green", bold_text=True)
        alert.alert("\nSuccessfully stored QR")




# Reading qr
class ReadQR():
    def __init__(self):
        
        self.name = "Read-QR"
        self.desciption = "Helps in reading QR-Code"
        self.theme = ["green", "blue"]

        # initializing makeqr mode
        self.mode = mandatum.Mode(
            name=self.name,
            description=self.desciption,
            theme=self.theme,
            bold_text=True
        )

        self.mode.init_prompt()
        
        self.prompt = self.mode.prompt

    def read_qr(self):
        print()
        self.mode.print_details()

        image_file = self.prompt.input("\nImage to read : ")

        alert = mandatum.Alert(color="red", bold_text=True)

        try:
            image_file = cv2.imread(get_image_path(image_file))

            detect = cv2.QRCodeDetector()
            text, array, dtype = detect.detectAndDecode(image_file)
            
            time.sleep(.5)
            console.print(f"[bold {self.theme[0]}]Detected QR : [bold {self.theme[1]}]{text}")

        except:
            time.sleep(.5)
            alert.alert(message="Can't read QR")



# prompt
prompt = mandatum.Prompt(color="yellow")





if __name__ == "__main__":
    while 1:
            
        # Running menu
        time.sleep(.5)
        print() 
        menu.start()
        
        # user choice
        choice = prompt.input("\nEnter Choice : ")

        # if choice == make qr
        if choice == "1":
            time.sleep(.5)
            make_qr = MakeQR()
            make_qr.mode.run(make_qr.make_qr)
        
        elif choice == "2":
            time.sleep(.5)
            read_qr = ReadQR()
            read_qr.mode.run(read_qr.read_qr)

        elif choice == "3":
            time.sleep(.5)
            exit()
        
        else:
            time.sleep(.5)
            alert = mandatum.Alert(color="red", bold_text=True)
            alert.alert(message="\nInvalid choice")