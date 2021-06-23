from pathlib import Path
from tkinter import (
    Button,
    Entry,
    Label,
    OptionMenu,
    StringVar,
    Tk,
    filedialog,
    messagebox,
    simpledialog,
    ttk,
)
from typing import Any, Dict, Optional

root = Tk()


def get_filepath(prompt: str = "", init_dir: str = Path(__file__).parent.as_posix()):
    """


    :param prompt:  (Default value = "")
    :param init_dir:  (Default value = Path(__file__).parent.as_posix())

    """
    try:
        # root = Tk()
        # root.withdraw()
        filepath = filedialog.askopenfilename(title=prompt, initialdir=init_dir, parent=root)
    except Exception as e:
        print(e)
        filepath = ""
    return filepath


def get_directory_path(
        prompt: str = "", init_dir: str = Path(__file__).parent.as_posix()
) -> str:
    """


    :param prompt:  (Default value = "")
    :type prompt: str
    :param init_dir:  (Default value = Path(__file__).parent.as_posix())
    :type init_dir: str
    :rtype: str

    """
    try:
        # root = Tk()
        # root.withdraw()
        dir_path = filedialog.askdirectory(title=prompt, initialdir=init_dir, parent=root)
    except Exception as e:
        print(e)
        dir_path = ""
    return dir_path


class TkinterForm:
    """ """

    def __init__(self, dict_to_convert_to_form: Dict[str, str], default_form_vals:Optional[Dict[Any,Any]]=None) -> None:
        """


        :param dict_to_convert_to_form:
        :type dict_to_convert_to_form: Dict[str, str]
        :rtype: None

        """
        self.dict_to_convert_to_form = dict_to_convert_to_form.copy()
        if default_form_vals is None:
            default_form_vals = {}
        self.default_form_vals = default_form_vals
        self.submitted_form_values = {}

        # root = Tk()
        self.root = root
        self.string_variables = {}
        self.create_form_from_dict()
        self.root.mainloop()

    def copy_string_var_values(self) -> None:
        """



        :rtype: None

        """
        for k, v in self.string_variables.items():
            val_entered = v.get()
            self.submitted_form_values[k] = val_entered
        self.root.quit()

    def create_form_from_dict(self) -> None:
        """



        :rtype: None

        """
        i = 0
        for i, k in enumerate(self.dict_to_convert_to_form.keys()):
            label_text_to_use = self.dict_to_convert_to_form[k]
            name_var = StringVar()
            name_label = Label(
                self.root, text=label_text_to_use, font=("calibre", 10, "bold")
            )
            if isinstance(self.default_form_vals.get(k, ""), list):
                values = self.default_form_vals.get(k)
                name_var.set(values[0])
                someStyle = ttk.Style()
                font_dict = {"font": ("calibre", 10, "normal")}
                someStyle.configure('selection_option', **font_dict)
                name_entry = OptionMenu(self.root, name_var, *values)
                name_entry['menu'].configure(**font_dict)
            else:
                name_entry = Entry(
                    self.root, textvariable=name_var, font=("calibre", 10, "normal")
                )
            name_label.grid(row=i, column=0)
            name_entry.grid(row=i, column=1)

            self.string_variables[k] = name_var
        sub_btn = Button(self.root, text="Submit", command=self.copy_string_var_values)
        sub_btn.grid(row=i + 1, column=1)


def ask_string(title: str = "foo", prompt: str = "bar", **kwargs) -> str:
    str_input = simpledialog.askstring(title=title, prompt=prompt, parent=root, **kwargs)
    if str_input is None:
        str_input = ""
    return str_input


def show_info_message(title="", message="", **kwargs):
    messagebox.showinfo(title=title, message=message, parent=root, **kwargs)


def destroy_root():
    try:
        root.destroy()
    except Exception as e:
        root.quit()
        root.destroy()
        print(e)
