import view
import model
import logger

def push_button():
    # while True:
    mode=view.choose_mode()
    print(f'{mode} присвоено значение')        
    if mode==1:
        contact=view.serch_contact()
        base=logger.open_base()
        result=model.search_contact(base,contact)
        view.show_contact(result)
    elif mode==2:
        contact=view.new_contact()
        logger.add_contact(contact)
            

