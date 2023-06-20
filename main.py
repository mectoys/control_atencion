
from flask import Flask
from config import config
from scr.models.entities.Attention_Control import Attention_Control
from scr.models.model_Attention_Control import model_Attention_Control
app= Flask(__name__)



if __name__ == '__main__':
    #model_Attention_Control.get_attention_control_list()
    app.config.from_object(config['development'])

    app.run()

