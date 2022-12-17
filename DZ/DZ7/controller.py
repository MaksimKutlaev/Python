import view
import model
import logger

def push_button():
    resume=True
    while resume:
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
        is_resume=view.resume_app()
        if is_resume==1:
            resume=True
        elif is_resume==2:
            resume=False
        else:
            print('Вводите только 1 или 2')
        
            

