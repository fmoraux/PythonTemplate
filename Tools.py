# -*- coding: utf-8
# coding: utf-8
# ==========================================================================
# =====    Script         : Outils                                     =====
# =====    Author         : Flavie MORAUX (moraux.flavie@gmail.com)    =====
# ==========================================================================
import os
import getpass

from Tools.ConfigTool import ConfigTools
from Tools.CryptoTool import CryptoTool
from Tools.LogTool import LogTool
# --------------------------------------------------

DEFAULT_DIR_LOG = "Log"
DEFAULT_DIR_RESULT = "Result"

def _check_param_folder(folder, folder_default):
    """
    Vérification d'un paramètre de type dossier
    :param folder: Chemin à vérifier
    :param folder_default: Nom de dossier par défaut
    :return: Chemin du dossier vérifié
    """
    check_folder = None
    if os.path.isabs(folder):
        # Cas d'un chemin absolu
        check_folder = folder
    elif folder != None and len(folder) > 0:
        # Cas d'un chemin relatif
        script_dir_path = os.path.dirname(os.path.realpath(__file__))
        check_folder = os.path.join(script_dir_path, folder)
    else:
        # Cas d'un chemin non renseigné
        script_dir_path = os.path.dirname(os.path.realpath(__file__))
        check_folder = os.path.join(script_dir_path, folder_default)
    # end if
    
    # Test si le dossier existe, sinon on le créé
    if not os.path.exists(check_folder):
        os.mkdir(check_folder)
    # end if
    
    return check_folder
# end def _check_param_folder

# --------------------------------------------------

def encode_password():
    """
    Encodage d'un mot de passe
    """
    # Initialisation de la configuration
    script_dir_path = os.path.dirname(os.path.realpath(__file__))
    config_file_path = os.path.join(script_dir_path, "Configuration.ini")
    config = ConfigTools(config_file_path)

    # Initialisation des logs
    log_path = _check_param_folder(config.get_value("MAIN", "LOG_DIR"), "Log")
    LogTool(printFlag=True, loggingFlag=True, loggingDirPath=log_path)
    LogTool.instance().init("Encodage d'un mot de passe")

    # Demande du mot de passe
    password = getpass._raw_input("Mot de passe à encoder ?")
    if password != None and len(password) > 0:
        LogTool.instance().add_info("Mot de passe à encoder : {}".format(password))
        password_encoded = CryptoTool.encode(password)
        LogTool.instance().add_info("Mot de passe encodé : {}".format(password_encoded.decode("utf-8")))
    # end if

    LogTool.instance().finalize()
# end def encode_password

# --------------------------------------------------
