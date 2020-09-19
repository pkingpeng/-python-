import pyautogui


def click_by_list(source_list, duration):
    for node in source_list:
        print('click %s' % node[0])
        pyautogui.click(node[1], duration=duration)
