import flet as ft
from database.corso_DAO import getAllCorsi

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None
        self._page.horizontal_alignment = 'CENTER'

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name

        #POPOLO IL MENU A TENDINA
        corsi = getAllCorsi()
        options = []
        for corso in corsi.keys():
            option = ft.dropdown.Option(key= corso, text=corsi[corso].__str__())
            options.append(option)
        self._dropdown = ft.Dropdown(
            label="Scegli un'opzione",
            options=options,
            on_change=self.controller.on_change_dropdown
        )
        self._btnCercaIscritti=ft.ElevatedButton(text="Cerca iscritti", on_click=self.controller.on_cercaIscritti)
        row1 = ft.Row([self._dropdown, self._btnCercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        #row 2 text field
        self._txtMat = ft.TextField(label= "Matricola", color="blue")
        self._txtNome = ft.TextField(label= "Nome", color="blue", read_only=True)
        self._txtCognome = ft.TextField(label= "Cognome", color="blue", read_only=True)

        row2 = ft.Row([self._txtMat, self._txtNome, self._txtCognome], alignment=ft.MainAxisAlignment.CENTER)

        #row 3 buttons
        self._btnCercaStudente = ft.ElevatedButton(text="Cerca studente", on_click=self.controller.on_cercaStudente)
        self._btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi", on_click=self.controller.on_cercaCorsi)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi")
        self._btnReset = ft.ElevatedButton(text="Reset", on_click=self.controller.on_reset)

        row3 = ft.Row([self._btnCercaStudente, self._btnCercaCorsi, self._btnIscrivi, self._btnReset], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2, row3)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller


    def update_page(self):
        self._page.update()
