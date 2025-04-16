import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.lv = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.corsoSelezionato = None
        self.matSelezionata = None

    def on_change_dropdown(self, e):
        self.corsoSelezionato = self._model._corsi[self._view._dropdown.value]

    def on_changeTxtMatricola(self):
        matricola = self._view._txtMat.value
        try:
            matricola = int(matricola)
            return matricola
        except ValueError:        #alert dialog fatto con deepseek
            self._view._page.dialog = ft.AlertDialog(
                title=ft.Text("Attenzione!", color="red"),
                content=ft.Text(
                    "Formato matricola errato\ninserire una matricola valida"),
                open=True
            )
            self._view.update_page()
            return None

    def on_cercaIscritti(self, e):
        if self.lv is not None:
            self._view._page.controls.remove(self.lv)
        txt = ""
        self.lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        iscrittiCorso = self._model.cercaIscritti(self.corsoSelezionato)
        if iscrittiCorso is None:          #alert dialog fatto con deepseek
            self._view._page.dialog = ft.AlertDialog(
                title=ft.Text("Attenzione!", color= "red"),
                content=ft.Text(
                    "Nessun corso selezionato.\nSeleziona un corso dalla lista prima di cercare gli iscritti."),
                open=True
            )
        else:
            txt = f"Nel corso ci sono {len(iscrittiCorso)} alunni iscritti"
            self.lv.controls.append(ft.Text(txt))
            for studente in iscrittiCorso:
                self.lv.controls.append(ft.Text(f"\n{self._model._studenti[studente._matricola]}"))

        self._view._page.add(self.lv)

    def on_cercaStudente(self, e):
        matricola = self.on_changeTxtMatricola()
        if matricola is None:
            return

        if matricola >= 1000000:        #alert dialog fatto con deepseek
            self._view._page.dialog = ft.AlertDialog(
                title=ft.Text("Attenzione!", color="red"),
                content=ft.Text(
                    "Formato matricola errato\ninserire una matricola valida"),
                open=True
            )
            self._view.update_page()
            return

        studente = self._model.cercaStudente(matricola)
        if studente is None:          #alert dialog fatto con deepseek
            self._view._page.dialog = ft.AlertDialog(
                title=ft.Text("Attenzione!", color= "red"),
                content=ft.Text(
                    "Matricola inesistente.\nSeleziona una matricola presente nel database"),
                open=True
            )
            self._view.update_page()
            return
        else:
            self._view._txtNome.value = studente._nome
            self._view._txtCognome.value = studente._cognome
            self._view.update_page()

    def on_cercaCorsi(self, e):
        matricola = self.on_changeTxtMatricola()
        if matricola is None:
            return

        if matricola >= 1000000:        #alert dialog fatto con deepseek
            self._view._page.dialog = ft.AlertDialog(
                title=ft.Text("Attenzione!", color="red"),
                content=ft.Text(
                    "Formato matricola errato\ninserire una matricola valida"),
                open=True
            )
            self._view.update_page()
            return

        corsiStudente = self._model.cercaCorsi(matricola)

        if len(corsiStudente) == 0:
            self._view._page.dialog = ft.AlertDialog(
                title=ft.Text("Attenzione!", color="red"),
                content=ft.Text(
                    "Lo studente non è iscritto a nessun corso"),
                open=True
            )
            self._view.update_page()
            return
        else:
            if self.lv is not None:
                self._view._page.controls.remove(self.lv)
            self.lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
            txt = f"Lo studente è iscritto a {len(corsiStudente)} corsi"
            self.lv.controls.append(ft.Text(txt))
            for studente in corsiStudente:
                self.lv.controls.append(ft.Text(f"\n{studente.__str__()}"))

        self._view._page.add(self.lv)

    def on_reset(self, e):
        self._view._page.controls.clear()
        self._view.load_interface()




