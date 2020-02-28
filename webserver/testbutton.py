from gpiozero import Button

button = Button(17) 

button.wait_for_press()
print("working")
# while True:
#     if button.is_pressed:
#         print("Button pressed ")

#     else: 
#         print("Button is not pressed")

    