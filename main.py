#####################################
#   Learn Vocabulary - 15/2/24      #
#####################################
# NOTES :
"""
"""
# -- IMPORTS --
# Modules
from utility import *
from voc_managing_functions.functions import *
import logging
# Classes

# Logging
logger = Settings.setup_logging("main")
logger.info("Start")

# -- Variables Globales --


# -- FONCTIONS DÉFINIES --
def choose_location_for_input_words():
    new_dir_location = File.ask_dir()
    if new_dir_location is None or not os.path.exists(new_dir_location):
        logger.error(f"OP:Change Location: CANCELED (DirNotFound: {new_dir_location})")
        return
    new_file_path = os.path.join(new_dir_location, "new_words.txt")
    File.JsonFile.set_value_jsondict("main_settings.json", "global", new_file_path,
                                     can_modify_key=True, can_add_key=False)
    logger.info(f"OP:Change Location: CHANGED ({new_file_path})")
    File.create_file_tree(new_file_path, can_make_dirs=False)


def actualiser_mots():
    logger.info("Actualisation des mots")
    # 1 - Trouver les nouveaux mots
    source_path = File.JsonFile.get_value_jsondict("main_settings.json", "global", handle_keyERROR=False)
    with open(source_path, "r", encoding='utf-8') as file:
        extraction = file.read().split("\n")
    new_words = [word for word in extraction if word != ""]
    # 2 - Afficher les nouveaux mots
    for word in new_words:
        print(word.strip())
    logger.info("OP:Get Data: {} words ...\n{}".format(len(new_words), new_words))
    # 3 - Ajouter les nouveaux mots
    add_new_words(source_path)
    # 4 - Clear file
    with open(source_path, "w") as file:
        file.write("")
        logger.info("Get Data: list DELETED")


def create_cards():
    logger.info("Création de cartes")
    for class_name in ["english", "french"] :  # json.load(open("data/main_settings.json"))
        create_cards_from_waitlist(class_name, clear_source=True)


# -- VARIABLES INITIALES --
command_dict = {
    "Changer location": choose_location_for_input_words,
    "Actualiser mots": actualiser_mots,
    "Ajouter cartes": create_cards,
}

# -- FONCTIONS MAÎTRES --


# -- PROGRAMME --
if __name__ == '__main__':
    # - Variables -

    # - Programme -
    # Environnement
    establish_files()
    # Tableau de commandes
    wind = GUI.set_basic_window()
    GUI.set_cmd_buttons(wind, command_dict)
    wind.mainloop()
