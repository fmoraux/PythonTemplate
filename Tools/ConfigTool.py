# -*- coding: utf-8
#  coding: utf-8
# ==========================================================================
# =====    Script         : Script de configuration                    =====
# =====    Author         : Flavie MORAUX (moraux.flavie@gmail.com)    =====
# ==========================================================================
# Exemple d'utilisation :
#
#   ==> Côté configuration :
#   [ORGANISATION]
#   url=http://www.arcgis.com
#
#   ==> Côté code :
#   # Initialisation
#   configPath = r"C:\Temp\ArcGIS\AgolTools\Configuration.ini"
#   config = ConfigTools(configPath)
#   # Lecture du fichier
#   config.readConfig()
#   # Récupération d'un paramètre
#   param = config.get_value("ORGANISATION", "url")
# --------------------------------------------------
import os

from configparser import ConfigParser
# --------------------------------------------------
class ConfigTools(object):
    """Classe dédiée au fichier de configuration"""

    def __init__(self, config_path):
        """
        Initialisation de la configuration
        :param config_path: Chemin du fichier de configuration
        """
        self.__config_path = config_path
        self.__read_config()
    # end def __init__

    def __read_config(self):
        """
        Lecture du fichier de configuration
        :return:
        """
        self.__config_dct = {}

        if self.__config_path != None and os.path.exists(self.__config_path):
            config = ConfigParser()
            config.readfp(open(self.__config_path))

            # Parcours des sections ([BLABLA])
            for section in config.sections():

                # Parcours des clés de la section (BLABLA=VALUE)
                for (key, value) in config.items(section):
                    # TODO Résoudre le problème de la mise en minscule de la clé
                    # En attendant on ruse en repassant en majuscule, implique que les clés soient en majuscule dans le fichier
                    key = key.upper()
                    self.__config_dct[(section, key)] = value
                # end for

            # end for
        # end if
    # end def __read_config

    def get_value(self, section, key):
        """
        Retourne une valeur issue de la configuration
        :param section: Section de configuration
        :param key: Clé de configuration
        :return: Valeur ou None
        """
        value = None
        if section != None and len(section) != 0 and key != None and len(key) != 0 and self.__config_dct != None:
            if (section, key) in self.__config_dct.keys():
                value = self.__config_dct[(section, key)]
            # end if
        # end if
        return value
    # end def get_value

# end class ConfigTools
# --------------------------------------------------
