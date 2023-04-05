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


def renderingMinView():
    """
    Controls how information will be displayed in the minimal view
    """
    MAX_LENGTH = 31
    return



def renderingView(label: str) -> tuple[str, str]:
    """
    Controls how the information will be displayed in the view
    """
    MAX_LENGTH = 21

    if len(label) > 21:
        text = ""
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
    if view == "0" and num != ",":
        newText = num

    # check that only one comma can be placed
    elif num == ",":
        exists = False
        for c in range(len(view)):
            if view[c] == ",":
                exists = True

        if not exists:
            newText = view + num
        
        else:
            return

    # otherwise, it is added to the end of the string
    else:
        newText = view + num

    print(newText)
    # is displayed on screen
    text, buffer = renderingView(newText)
    gui.view.config(text=text)
    gui.buffer_view = buffer
    return


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
    bNumn(",")


def bDeny():

    return


def bEqual():

    return


def bAdd():

    return


def bSubtact():

    return


def bMultiply():

    return


def bSplit():

    return


def bClean():

    return


def bUndo():

    return


if __name__ == '__main__':
    # Window Loop
    gui.root.mainloop()
