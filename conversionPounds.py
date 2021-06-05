# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    import tkinter as tk

    def main():
        window = tk.Tk()
        window.title("Kilograms to Pounds to Calories Converter")
        window.geometry("375x200")

        # create a label with text Enter Kilograms
        label1 = tk.Label(window, text="Enter Kilograms:")

        # create a label with text Pounds:
        label2 = tk.Label(window, text="Pounds:")

        # place label1 in window at position x,y
        label1.place(x=50, y=30)

        # create an Entry widget (text box)

        textbox1 = tk.Entry(window, width=12)

        # place textbox1 in window at position x,y
        textbox1.place(x=200, y=35)

        # place label2 in window at position x,y
        label2.place(x=50, y=100)

        # create a label3 with empty text:
        label3 = tk.Label(window, text=" ")

        # place label3 in window at position x,y
        label3.place(x=180, y=100)

        def btn1_click():
            pounds  = round(float(textbox1.get()) * 2.20462, 5)
            label3.configure(text=str(pounds) + '  Pounds')

        # create a button with text Button 1
        btn1 = tk.Button(window, text="Click Me To Convert", command=btn1_click)
        # place this button in window at position x,y
        btn1.place(x=90, y=150)
        window.mainloop()

    main()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Dancers divide each pound by 3500 calories to get weight loss ')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

