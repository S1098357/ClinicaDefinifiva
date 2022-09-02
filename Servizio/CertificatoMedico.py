import os.path
import pickle

from Servizio.Documento import Documento


class CertificatoMedico(Documento):

    def __init__(self):
        super().__init__()
        self.prezzo=25

    def compilaCertificato(self,nomePaziente,nomeCognomeDottore,dataRilascio):
        self.CompilaDocumento(nomePaziente,nomeCognomeDottore,dataRilascio)

    def stampaCertificato(self):
        #documento=self.StampaDocumento()
        #documento['importoPagato']=self.prezzo
        #if os.path.isfile('dati/Certificati.pickle'):
        with open ('dati/Certificati.pickle' , 'wb+') as f:
            pickle.dump(self,f,pickle.HIGHEST_PROTOCOL)
        #else:
            #with open ("dati/Ricetta.pickle",'xb') as f:
                #pickle.dump(ricetta,f,pickle.HIGHEST_PROTOCOL)

    def leggiCertificato(self):
        if os.path.isfile ('dati/Certificati.pickle') :
            with open ('dati/Certificati.pickle' , 'rb+') as f:
                return pickle.load(f)
        else:
            return False