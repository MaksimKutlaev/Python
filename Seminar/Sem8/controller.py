import logger
import model
import view
import test


def run ():
    while True:
        mod = view.choice_mode()
        if mod =='1': # создание контакта
            contact = view.new_contact()
            logger.update_base(contact)
        elif mod =='2': # поиск контакта
            contact = view.choice_mode()
            base = logger.get_base()
            result = model.find_contacts(base, contact)
            view.show_found(result)
        elif mod =='3': # редактирование контакта
            contact = view.choice_mode()
            base = logger.get_base()
            result = model.find_contacts(base, contact)
            view.show_found(result)
            result = model.edit_str(base, result)


        elif mod =='4': # удаление контакта
            contact = view.choice_mode()
            base = logger.get_base()
            result = model.find_contacts(base, contact)
            base = logger.del_base()
            # contact = delete_contact()
            # LoggerNew.delete_contact