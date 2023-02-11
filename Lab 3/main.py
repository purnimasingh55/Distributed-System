# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

''''

server: 
bind()
listen() // no. of connection he client can connect
accept()
send()
recieve() //both side

client
connect
send()
recieve()

in UDP connect() is not required client side connection name become DGRAM:
    client need not to be active and listen thus listen function also not required
    accept also not reqired
    
'''