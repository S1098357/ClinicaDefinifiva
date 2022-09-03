import datetime
from unittest import TestCase

from Amministrazione.Segreteria import Segreteria
from Amministrazione.Sistema import Sistema
from Servizio.Prenotazione import Prenotazione


class TestPrenotazione(TestCase):

    def testNuovaPrenotazione(self):
        self.prenotazione=Prenotazione()
        self.prenotazione.cliente='prova'
        self.prenotazione.dataOra=datetime.datetime.now()
        sistema=Sistema([])
        sistema.listaPrenotazioni=[self.prenotazione]
        sistema.salvaPrenotazioni()
        sistema.leggiPrenotazioni()
        self.assertEqual(self.prenotazione,sistema.listaPrenotazioni[0])

    def testEliminaPrenotazione(self):
        self.prenotazione = Prenotazione()
        self.prenotazione.cliente = 'prova'
        self.prenotazione.dataOra = datetime.datetime.now()
        segreteteria = Segreteria()
        segreteteria.x.listaPrenotazioni = [self.prenotazione]
        segreteteria.eliminaPrenotazione(self.prenotazione)
        segreteteria.x.leggiPrenotazioni()
        for prenotazione in segreteteria.x.listaPrenotazioni:
            self.assertNotEqual(prenotazione,self.prenotazione)
