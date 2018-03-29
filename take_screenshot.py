import pyscreenshot as ImageGrab
import datetime

if __name__ == "__main__":
    # fullscreen
    #while True:
    im=ImageGrab.grab()
        # save image file
    im.save('D://Luis/Screenshots/screenshot'+datetime.datetime.now().strftime ("%Y%m%d_%H%M%S")+'.png')
    #im.show()
#-#