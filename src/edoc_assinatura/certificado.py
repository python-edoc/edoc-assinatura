# coding=utf-8

from OpenSSL import crypto


class Certificado(object):

    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def abre_arquivo(self):
        return open(self.caminho_arquivo, 'rb')

    def separa_chave_certificado(self, senha):
        """ Realiza a separação da chave e do certificado

        :param senha:
        :return:
        """
        p12 = crypto.load_pkcs12(self.abre_arquivo().read(), senha)
        certificado = crypto.dump_certificate(crypto.FILETYPE_PEM,
                                              p12.get_certificate())
        chave = crypto.dump_privatekey(crypto.FILETYPE_PEM,
                                       p12.get_privatekey())
        return chave, certificado

    def p12(self, senha):
        """ 
        :param senha:
        :return:
        """
        return crypto.load_pkcs12(self.abre_arquivo().read(), senha)
