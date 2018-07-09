# -*- coding: utf-8
# coding: utf-8
# ==========================================================================
# =====    Script         : Script d'encodage                          =====
# =====    Author         : Flavie MORAUX (moraux.flavie@gmail.com)    =====
# ==========================================================================
# Exemple d'utilisation :
#
#   ==> Côté code :
#   valueToEncypt = "Test"
#   print ("valueToEncypt={}".format(valueToEncypt))
#   valueEncrypted = CryptoTool.Encode(valueToEncypt)
#   print ("valueEncrypted={}".format(valueEncrypted))
#   valueDecrypted = CryptoTool.Decode(valueEncrypted)
#   print ("valueDecrypted={}".format(valueDecrypted))
#
#   ==> Côté résultat :
#   valueToEncypt=Test
#   valueEncrypted=b'VGVzdA=='
#   valueDecrypted=Test
# --------------------------------------------------
import base64
# --------------------------------------------------

class CryptoTool(object):
    """Classe dédiée au cryptage"""

    ENCODING = "utf-8"

    @staticmethod
    def encode(value):
        """
        Encodage d'une valeur
        :param value: Valeur à encoder
        :return: Valeur encodée
        """
        encode_value = None
        if value != None:
            encode_value = base64.b64encode(bytes(value))
        # end if
        return encode_value
    # end def encode

    @staticmethod
    def decode(encode_value):
        """
        Décodage d'une valeur
        :param encode_value: Valeur à décoder
        :return: Valeur décodée
        """
        value = None
        if encode_value != None:
            value = base64.b64decode(encode_value).decode(CryptoTool.ENCODING)
        # end if
        return value
    # end def decode

# end class CryptoTool
# --------------------------------------------------
