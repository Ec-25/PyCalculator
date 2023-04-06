import gui


def action():
    print("ACTION")
    return


def concatCheck(label: str) -> bool:
    """
    False = Need operate.\n
    True = Concatenate more numbers.
    """
    if label[-1] in "+-*/":
        return False
    return True


def rendering(label: str, general:bool = True) -> tuple[str, str]:
    """
    Controls how the information will be displayed in the view
    General = True: MAX_LENGTH = 21 for View
    General = False: MAX_LENGTH = 31 for MinView
    """
    if general:
        MAX_LENGTH = 21
    else:
        MAX_LENGTH = 31

    if len(label) > MAX_LENGTH:
        text = ""
        # All the numbers remain in the buffer, and only the last 21 digits are shown
        for i in range(MAX_LENGTH):
            if len(text) == 0:
                text = label[-1-(i)]
            else:
                text = label[-1-(i)] + text

        return text, label

    else:
        # text, buffer
        return label, label


def bNumn(num: str) -> None:
    # get Label Text
    view = gui.buffer_view
    newText = ""

    # if it is equal to zero, it is replaced by the income
    if view == "0" and num != ".":
        newText = num

    # check that only one comma can be placed
    elif num == ".":
        exists = False
        for c in range(len(view)):
            if view[c] == ".":
                exists = True

        if not exists:
            newText = view + num
        
        else:
            return

    # otherwise, it is added to the end of the string
    else:
        newText = view + num

    # is displayed on screen
    text, buffer = rendering(newText)
    gui.view.config(text=text)
    gui.buffer_view = buffer


def b0():
    bNumn("0")


def b1():
    bNumn("1")


def b2():
    bNumn("2")


def b3():
    bNumn("3")


def b4():
    bNumn("4")


def b5():
    bNumn("5")


def b6():
    bNumn("6")


def b7():
    bNumn("7")


def b8():
    bNumn("8")


def b9():
    bNumn("9")


def bPoint():
    bNumn(".")


def bDeny():
    # get buffer of view
    view = gui.buffer_view

    # If the number is negative, remove the sign
    if view[0] == "-":
        view = view[1:]

    # otherwise, the negative sign is added
    else:
        view = "-" + view

    # the buffer is saved again and set as shown
    gui.buffer_view = view

    text, buffer = rendering(view)
    gui.view.config(text=text)
    gui.buffer_view = buffer


def bEqual():
    bView = gui.buffer_view
    # if bView != "0":



def bAdd():
    # get buffer of view and buffer of min_view
    bView = gui.buffer_view
    bMin_view = gui.buffer_min_view

    exists = False
    for i in range(len(bMin_view)):
        if bMin_view[i] == "+":
            exists = True

    # If the min view already has the symbol, add it and put the symbol back, if not, just put the number and the operation
    if exists:
        if bView != "0" and bMin_view != "0":
            bView = float(bView)
            bMin_view = float(bMin_view[:-1])
            result = bMin_view + bView

        elif bView != "0" and bMin_view == "0":
            bView = float(bView)
            bMin_view = int(bMin_view)
            result = bMin_view + bView

        else:
            # if you have not yet indicated a value, do nothing
            return
        if str(result)[-2:] == ".0":
            result = str(result)[:-2]
            result = int(result)

        result = round(result, 2)
        result = str(result) + "+"
    
    else:
        bView = float(bView)
        bMin_view = int(bMin_view)
        result = bMin_view + bView

        if str(result)[-2:] == ".0":
            result = str(result)[:-2]
            result = int(result)

        result = round(result, 2)
        result = str(result) + "+"

    # update views and buffers
    gui.buffer_view = "0"
    gui.view.config(text="0")

    text, buffer = rendering(str(result), False)
    gui.buffer_min_view = buffer
    gui.min_view.config(text=text)


def bSubtact():

    return


def bMultiply():

    return


def bSplit():

    return


def bClean():
    # set all view labels to 0
    if gui.buffer_view == "0":
        gui.buffer_min_view = "0"
        gui.min_view.config(text="")
    gui.buffer_view = "0"
    gui.view.config(text="0")


def bUndo():
    # removes the last element from the view tag
    gui.buffer_view = gui.buffer_view[:-1]
    text:str = gui.view.cget("text")
    gui.view.config(text=text[:-1])


if __name__ == '__main__':
    # Window Loop
    gui.root.mainloop()
