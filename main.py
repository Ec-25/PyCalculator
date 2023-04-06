import gui


def action():
    print("ACTION")
    return


def updateViews(minView:str):
    # update views and buffers
    gui.buffer_view = "0"
    gui.view.config(text="0")

    updateMinView(minView)


def updateMinView(minView:str):
    # update only min view
    text, buffer = rendering(minView, False)
    gui.buffer_min_view = buffer
    gui.min_view.config(text=text)


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

    # if there is no digit, it is like saying that the number is zero
    if len(view) == 0:
        view = "0"

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
    bMinView = gui.buffer_min_view
    if not(bView != "0" and bMinView[-1] == "/") and bMinView[-1] in "+-*/":
        if bMinView[-1] == "+":
            result = float(bMinView[:-1]) + float(bView)
        elif bMinView[-1] == "-":
            result = float(bMinView[:-1]) - float(bView)
        elif bMinView[-1] == "*":
            result = float(bMinView[:-1]) * float(bView)
        elif bMinView[-1] == "/":
            result = float(bMinView[:-1]) / float(bView)

        result = round(result, 2)
        if str(result)[-2:] == ".0":
            result = str(result)[:-2]
            result = int(result)

        updateViews(str(result))


def bAdd():
    # get buffer of view and buffer of min_view
    bView = gui.buffer_view
    bMin_view = gui.buffer_min_view

    exists = False
    for i in range(len(bMin_view)):
        if bMin_view[i] == "+":
            exists = True
        
        # If there is another previous operation, it is first resolved and then the symbol of the operation is added
        elif i != 0 and bMin_view[i] in "-*/":
            bEqual()
            bMin_view = gui.buffer_min_view
            bMin_view = bMin_view + "+"
            updateMinView(bMin_view)
            return

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
        try:
            bMin_view = float(bMin_view)
        except ValueError:
            try:
                bMin_view = int(bMin_view)
            except ValueError:
                bMin_view = int(bMin_view[:-1])
        result = bMin_view + bView

        if str(result)[-2:] == ".0":
            result = str(result)[:-2]
            result = int(result)

        result = round(result, 2)
        result = str(result) + "+"

    # update views and buffers
    updateViews(str(result))


def bSubtact():
    # get buffer of view and buffer of min_view
    bView = gui.buffer_view
    bMin_view = gui.buffer_min_view

    exists = False
    for i in range(len(bMin_view)):
        if bMin_view[i] == "-":
            exists = True

        # If there is another previous operation, it is first resolved and then the symbol of the operation is added
        elif bMin_view[i] in "+*/":
            bEqual()
            bMin_view = gui.buffer_min_view
            bMin_view = bMin_view + "-"
            updateMinView(bMin_view)
            return

    # If the min view already has the symbol, subtract it and put the symbol back, if not, just put the number and the operation
    if exists:
        if bView != "0" and bMin_view != "0":
            bView = float(bView)
            bMin_view = float(bMin_view[:-1])
            result = bMin_view - bView

        elif bView != "0" and bMin_view == "0":
            bView = float(bView)
            bMin_view = int(bMin_view)
            result = bMin_view - bView

        else:
            # if you have not yet indicated a value, do nothing
            return
        if str(result)[-2:] == ".0":
            result = str(result)[:-2]
            result = int(result)

        result = round(result, 2)
        result = str(result) + "-"
    
    else:
        bView = float(bView)
        try:
            bMin_view = float(bMin_view)
        except ValueError:
            try:
                bMin_view = int(bMin_view)
            except ValueError:
                bMin_view = int(bMin_view[:-1])

        if bMin_view != 0:
            result = bMin_view - bView
        else:
            result = bView

        if str(result)[-2:] == ".0":
            result = str(result)[:-2]
            result = int(result)

        result = round(result, 2)
        result = str(result) + "-"

    # update views and buffers
    updateViews(str(result))


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
