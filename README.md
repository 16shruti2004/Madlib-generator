# Mad Libs Generator

Welcome to the Mad Libs Generator! This is a fun and interactive application built using Python's tkinter library. The generator provides three different Mad Libs stories where you can input various words to create hilarious and unique tales.

## Features
- Interactive user interface created with tkinter
- Three predefined Mad Libs stories
- Validations for input to ensure words are chosen from predefined sets
- Fun and educational activity for all ages

## How to Run
1. Clone the Repository:
    ```bash
    git clone https://github.com/your-repository.git
    ```
   
2. Navigate to the Directory:
    ```bash
    cd your-repository
    ```

3. Run the Code:
    ```bash
    python Madlib_Generator_Application.py
    ```

## User Instructions
1. Run the application.
2. Choose any one of the provided stories by clicking on the respective button.
3. Follow the prompts and enter your choices for nouns, verbs, adjectives, and other inputs.
4. Enjoy your unique and funny Mad Libs story!

## Code Structure
- Importing Modules:
    ```python
    from tkinter import *
    ```

- Initialize Window:
    ```python
    root = Tk()
    root.geometry('300x300')
    root.title('Fun with Mad Libs!')
    ```

- Label Setup:
    ```python
    Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold').pack()
    Label(root, text='Click Any One :', font='arial 15 bold').place(x=40, y=80)
    ```

- Predefined Sets:
    - Nouns
    - Verbs
    - Adjectives

- Stories:
    - `madlib1()`: The Photographer
    - `madlib2(): The Butterfly
    - `madlib3()`: Apple and Apple

- Buttons:
    ```python
    Button(root, text='The Photographer', font='arial 15', command=madlib1, bg='ghost white').place(x=60, y=120)
    Button(root, text='Apple and Apple', font='arial 15', command=madlib3, bg='ghost white').place(x=70, y=180)
    Button(root, text='The Butterfly', font='arial 15', command=madlib2, bg='ghost white').place(x=80, y=240)
    ```

- Main Loop:
    ```python
    root.mainloop()
    ```

## How to Contribute
Feel free to fork this repository and submit pull requests. Contributions to enhance the code or add new stories are always welcome!

## License
This project is open source and available under the [MIT License](LICENSE).

---

Have fun creating your own Mad Libs stories!

How to execute - Type python MadlibGenerator_Application.py in Terminal and press ENTER.
