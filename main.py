
from ScreenCapture import ScreenCapture  

import matplotlib.pyplot as plt
from PIL import Image as pil_image
import pyautogui

from lite_classifier import LiteClassifier as NudeClassifierLite
from classifier import Classifier as NudeClassifier



#classifier = NudeClassifier()

classifier_lite = NudeClassifierLite()




capture = ScreenCapture()

screen_width, screen_height= capture.get_actual_screen_dimensions()


while True:
    
    screen = capture.get_screen()
    
    # Display the captured screen using matplotlib - You slow down the process
    '''
    pil_screen = pil_image.fromarray(screen)
    plt.imshow(pil_screen)
    plt.axis('off')  # Turn off axis
    plt.show(block=False)
    plt.pause(1)
    '''

    #classify = classifier.classify(screen)
    classify = classifier_lite.classify(screen)



    if not classify :
            print('---')
    else :        
        unsafe = classify[0]["unsafe"]
        safe =  classify[0]["safe"]
        print('safe : ' , safe )
        print('unsafe : ' , unsafe)
        if unsafe > 0.947 and safe < 0.05:
            print('safe : ' , safe )
            print('unsafe : ' , unsafe)
            print('sex ')
            pyautogui.press('right')
            pyautogui.press('right')
            #exit()
            exit()
        elif   unsafe > 0.6 :
            print('safe : ' , safe )
            print('unsafe : ' , unsafe)
            print('sex ')
            pyautogui.press('right')
            exit()

    #you can try by url img 
    #print(classifier_lite.classify('C:/Users/deep_root/Desktop/a.jpg'))
    

