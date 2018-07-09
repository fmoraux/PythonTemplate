# -*- coding: utf-8
# coding: utf-8
# ==========================================================================
# =====    Script         : Script de logging                          =====
# =====    Author         : Flavie MORAUX (moraux.flavie@gmail.com)    =====
# ==========================================================================
# Exemple d'utilisation : Test avec des log dans la console et dans un fichier de log
#
#   ==> Côté code :
#   logDirPath = r"C:\Temp\ArcGIS\AgolTools"
#   LogTool(printFlag=True, loggingFlag=True, loggingDirPath=logDirPath)
#   LogTool.Instance().addInfo("Ceci est un message")
#   LogTool.Instance().addWarning("Ceci est un warning")
#   LogTool.Instance().addError("Ceci est une erreur")
#
#   ==> Côté résultat :
#   [2017/12/01 10:51:04][INFO   ] Ceci est un message
#   [2017/12/01 10:51:04][WARNING] Ceci est un warning
#   [2017/12/01 10:51:04][ERROR  ] Ceci est une erreur
# --------------------------------------------------
import datetime
import logging
import os
# --------------------------------------------------

class LogTool(object):
    """Classe dédiée aux logs"""

    # Singleton
    _instance = None

    # Formattage de date utilisé ( console et fichier de log)
    DATE_FORMAT = "%Y%m%d-%H%M%S"
    # Formattage utilisé (fichier de log)
    LOGGING_FORMAT = "[%(asctime)s][%(levelname)s] %(message)s"
    # Niveau de log utilisé (fichier de log)
    LOGGING_LEVEL = logging.DEBUG

    def __new__(cls, *args, **kwargs):
        """
        Constructeur
        :param args:
        :param kwargs:
        :return:
        """
        if LogTool._instance is None:
            LogTool._instance = object.__new__(cls)
        # end if
        return LogTool._instance
    # end def __new__

    def __init__(self, printFlag=True, loggingFlag=False, loggingDirPath=None, loggingPrefix="Log", loggingDateSufix=True):
        """
        Initialisation
        :param printFlag: Flag pour l'ajout des messages dans la console
        :param loggingFlag: Flag pour l'ajout des messages dans un fichier de log
        :param loggingDirPath : Chemin du dossier où générer les logs
        :param loggingPrefix : Préfixe utilisé pour nommé le fichier de log
        :param loggingDateSufix : Flag utilisé pour suffixer le nom du fichier de log avec la date courante
        """
        self.__print_flag = printFlag
        self.__logging_flag = loggingFlag
        self.__logging_dir_path = loggingDirPath
        self.__logging_prefix = loggingPrefix
        self.__logging_date_sufix = loggingDateSufix

        # Initialisation du logger
        if self.__logging_flag:
            logging_name = self.__logging_prefix
            if self.__logging_date_sufix:
                logging_name += "_{}.log".format(datetime.datetime.now().strftime(LogTool.DATE_FORMAT))
            else:
                logging_name += ".log"
            # end if
            
            logging_path = os.path.join(self.__logging_dir_path, logging_name)
            logging.basicConfig(
                filename=logging_path,
                level=LogTool.LOGGING_LEVEL,
                format=LogTool.LOGGING_FORMAT,
                datefmt=LogTool.DATE_FORMAT
            )
        # end if
    # end def __init__
    
    def init(self, title):
        """
        Initialistaion du fichier de log
        :param title:Titre
        """
        self.add_info("==========================================================================")
        self.add_info(title)
        self.add_info("==========================================================================")
    # end def init
    
    def finalize(self):
        """
        Finalisation du fichier de log
        """
        self.add_info("==========================================================================")
    # end def finalize

    def add_info(self, message):
        """
        Ajout d'un message d'information
        :param message:Message
        :return:
        """
        if self.__print_flag:
            print("[{}][INFO   ] {}".format(self._get_date(), message))
        # end if
        if self.__logging_flag:
            logging.debug(message)
        # end if
    # end def add_info

    def add_warning(self, message):
        """
        Ajout d'un message d'alerte
        :param message:Message
        :return:
        """
        if self.__print_flag:
            print("[{}][WARNING] {}".format(self._get_date(), message))
        # end if
        if self.__logging_flag:
            logging.warning(message)
        # end if
    # end def add_warning

    def add_error(self, message):
        """
        Ajout d'un message d'erreur
        :param message:Message
        :return:
        """
        if self.__print_flag:
            print("[{}][ERROR  ] {}".format(self._get_date(), message))
        # end if
        if self.__logging_flag:
            logging.error(message)
        # end if
    # end def add_error

    def _get_date(self):
        """
        Retourne la date courante formatée
        :return: Date du jour formatée
        """
        return datetime.datetime.now().strftime(LogTool.DATE_FORMAT)
    # end def _get_date

    @staticmethod
    def instance():
        """
        Retourne l'instance de classe
        :return:
        """
        return LogTool._instance
    # end def instance
# end class LogTools
# --------------------------------------------------
