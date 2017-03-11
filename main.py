from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
import json
import os

from kivy.uix.screenmanager import ScreenManager, Screen

class BikeFitMobile(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(BikeFitMobile, self).__init__(**kwargs)

    def postSucess(self, req, result):
        text = Label(text="Dados salvos com sucesso!".format())
        pop_up = Popup(title="Sucesso!", content=text, size_hint=(.7, .7))
        pop_up.open()

    def postData(self, *args):
        self.params = json.dumps(
            {"nome": self.ids.nome.text,
             "email": self.ids.email.text,
             "telefone": self.ids.telefone.text,
             "cidade": self.ids.cidade.text,
             "endereco": self.ids.endereco.text,
             "data_nascimento": self.ids.data_nascimento.text,
             "cpf_cnpj": self.ids.cpf_cnpj.text,
             "ano_ini_esporte": self.ids.ano_ini_esporte.text,
             "modalidade_principal": self.ids.modalidade_principal.text,
             "vezes_treina": self.ids.vezes_treina.text,
             "duracao_treino": self.ids.duracao_treino.text,
             "horas_trein_semana": self.ids.horas_treina_semana.text,
             "rg": self.ids.rg.text,
             "modalidade_frequente": self.ids.modalidade_frequente.text,
             "duracao_treino_longo": self.ids.duracao_treino_longo.text,
             "profissao": self.ids.profissao.text,
             "competicoes_frequenta": self.ids.competicoes_frequenta.text,
             "duracao_provas": self.ids.duracao_provas.text,
             "tipo_de_relevo": self.ids.tipo_de_relevo.text,
             "nivel_atleta": self.ids.nivel_atleta.text,
             "outros": self.ids.outros.text}
        )

        self.headers = {'Content-type': 'application/json',
                        'Accept': 'application/json; charset=UTF-8',
                        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}

        self.req = UrlRequest('http://192.168.1.105:8000/api-atleta/', on_success=self.postSucess, req_body=self.params,
                              req_headers=self.headers)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            # self.text_input.text = stream.read()
            print(path, filename)

class CadastroAtleta(Screen):
    pass

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class bikeFitMobileApp(App):

    def build(self):
        main = BikeFitMobile()
        return main

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == '__main__':
    bikeFitMobileApp().run()