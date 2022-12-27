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
            # id=model.new_id(base,contact)
            logger.add_contact(contact)
        elif mode==3:
            contact=view.serch_contact()
            base=logger.open_base()
            result=model.search_contact(base,contact)
            view.show_contact(result)
            if 'не найден' not in result[0] and len(base.split('\n')) >1:
                result=model.search_contact(base,contact)
                new_contact=view.new_contact()
                upd=model.edit_contact(base,result[0],new_contact)
                logger.update_base(upd)
            elif 'не найден' not in result[0]:
                result=base.split('\n')[0]
                new_contact=view.new_contact()
                upd=model.edit_contact(base,result,new_contact)
                logger.update_base(upd)
        elif mode==4:
            contact=view.serch_contact()
            base=logger.open_base()
            result=model.search_contact(base,contact)
            view.show_contact(result)
            if 'не найден' not in result[0] and len(base.split('\n')) >1:
                result=model.search_contact(base,view.choice())[0]
                new_contact=view.new_contact()
                upd=model.del_contact(base,result,new_contact)
                logger.update_base(upd)
            elif 'не найден' not in result[0]:
                result=base.split('\n')[0]
                new_contact=view.new_contact()
                upd=model.edit_contact(base,result,new_contact)
                logger.update_base(upd)
        is_resume=view.resume_app()
        if is_resume==1:
            resume=True
        elif is_resume==2:
            resume=False