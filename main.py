from user import *

def main():
    user1=user("Omar")
    user2=user("Cyrine")
    user1.show_all_available_methods()
    user1.register()
    user1.show_all_available_methods()
    user1.chooseRoom()
    user1.show_all_available_methods()

    user1.join()
    user1.show_all_available_methods()
    user1.play()
    user1.show_all_available_methods()

    user1.QuitRoom()
    user1.show_all_available_methods()
    user1.unregister()
    user1.show_all_available_methods()
    user1.quit()
    user1.show_all_available_methods()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


