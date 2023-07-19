# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
from transformers import  pipeline
from sklearn.preprocessing import LabelEncoder
import random
import re
import string


paciente = random.randint(1, 3)
# Paciente 1: Hombre de 50 años llamado Mikel, acude a consulta por cancer de pulmon
# paciente 2: Mujer de 30 años llamada Janire, acude a consulta por envenenamiento de aracnido
# Paciente 3: Mujer de 44 años llamada Maitane, acude a consulta por resfriado l
model_name = "Mikelium5/DoctorIntentClassifier"
pipe = pipeline(model = model_name, tokenizer=model_name)
target = ['personal_dieta_frecuencia', 'personal_entorno_hijos_nombre', 'personal_adiccion_alcohol_describir', 'tratamiento_operacion_especialista', 'sintoma_paciente_secuela_si_o_no', 'tratamiento_medicacion_receta', 'otros', 'personal_deporte_si_o_no', 'tratamiento_diagnostico_fecha', 'sintoma_paciente_aparicion_describir', 'sintoma_paciente_embarazo_describir', 'sintoma_paciente_fiebre_describir', 'personal_dieta_duracion', 'personal_otros_describir', 'personal_entorno_pareja_si_o_no', 'personal_trabajo_si_o_no', 'tratamiento_operacion_describir', 'tratamiento_operacion_complicaciones', 'personal_fisico_peso_duracion', 'personal_datos_direccion', 'tratamiento_operacion_dosis', 'sintoma_paciente_seguimiento_si_o_no', 'sintoma_paciente_localizacion_describir', 'personal_adiccion_alcohol_cantidad', 'sintoma_paciente_inicio', 'tratamiento_medicacion_frecuencia', 'personal_entorno_hijos_edad', 'despedida', 'tratamiento_consulta_describir', 'personal_dieta_si_o_no', 'personal_sueño_si_o_no', 'tratamiento_operacion_frecuencia', 'personal_adiccion_fumar_duracion', 'personal_datos_edad', 'vida_sexual_si_o_no', 'personal_entorno_hijos_si_o_no', 'personal_entorno_describir', 'personal_adiccion_otros_describir', 'tratamiento_medicacion_otros', 'tratamiento_anticonceptivos_describir', 'personal_trabajo_describir', 'personal_entorno_pareja_otros', 'personal_dieta_cuando', 'vida_sexual_frecuencia', 'sintoma_paciente_embarazo_antecedentes', 'personal_entorno_mascota_si_o_no', 'personal_deporte_describir', 'personal_adiccion_alcohol_frecuencia', 'tratamiento_operacion_resultados', 'personal_trabajo_lugar', 'personal_contacto', 'sintoma_paciente_embarazo_si_o_no', 'personal_deporte_cantidad', 'sintoma_paciente_frecuencia', 'personal_entorno_hijos_otros', 'personal_adiccion_fumar_inicio', 'personal_viajes_si_o_no', 'sintoma_paciente_antecedentes_describir', 'tratamiento_historial_si_o_no', 'sintoma_paciente_capacidad_describir', 'personal_sueño_horas', 'sintoma_paciente_causa_si_o_no', 'tratamiento_operacion_fecha', 'personal_entorno_padres_si_o_no', 'personal_fisico_peso_peso', 'personal_deporte_cuando', 'sintoma_paciente_duracion', 'sintoma_familia_inicio', 'sintoma_bebe_si_o_no', 'personal_entorno_otros_describir', 'psiquiatria_estado de animo_si_o_no', 'sintoma_paciente_secuela_describir', 'tratamiento_medicacion_cuando', 'tratamiento_historial_describir', 'tratamiento_medicacion_dosis', 'sintoma_paciente_aparicion_si_o_no', 'sintoma_paciente_localizacion_si_o_no', 'tratamiento_diagnostico_como', 'vida_sexual_describir', 'vida_sexual_edad', 'sintoma_paciente_describir', 'personal_entorno_pareja_nombre', 'sintoma_paciente_si_o_no', 'personal_adiccion_fumar_cantidad', 'sintoma_familia_describir', 'sintoma_paciente_embarazo_otros', 'tratamiento_diagnostico_si_o_no', 'sintoma_bebe_peso', 'saludo', 'sintoma_paciente_embarazo_cantidad', 'tratamiento_consulta_fecha', 'personal_fisico_peso_cambio', 'tratamiento_medicacion_motivo', 'sintoma_paciente_causa_describir', 'personal_fisico_altura', 'sintoma_paciente_alergia_si_o_no', 'personal_datos_fecha_de_nacimiento', 'personal_deporte_frecuencia', 'personal_adiccion_alcohol_otros', 'psiquiatria_estado de animo_describir', 'personal_trabajo_otros', 'personal_adiccion_fumar_frecuencia', 'personal_adiccion_alcohol_si_o_no', 'tratamiento_consulta_si_o_no', 'personal_dieta_otros', 'motivo_de_consulta', 'personal_adiccion_otros_si_o_no', 'sintoma_paciente_antecedentes_si_o_no', 'personal_entorno_otros_si_o_no', 'personal_otros_si_o_no', 'personal_viajes_describir', 'personal_dieta_cantidad', 'vida_sexual_otros', 'sintoma_paciente_cambio_describir', 'personal_datos_nombre', 'tratamiento_anticonceptivos_si_o_no', 'estado', 'sintoma_paciente_alergia_describir', 'tratamiento_operacion_si_o_no', 'personal_trabajo_anterior', 'sintoma_entorno_si_o_no', 'personal_adiccion_fumar_si_o_no', 'tratamiento_medicacion_describir', 'tratamiento_anticonceptivos_frecuencia', 'sintoma_familia_si_o_no', 'tratamiento_operacion_motivo', 'personal_entorno_hijos_describir', 'personal_trabajo_duracion', 'personal_adiccion_alcohol_duracion', 'personal_sueño_describir', 'sintoma_paciente_capacidad_si_o_no', 'sintoma_paciente_fiebre_si_o_no', 'sintoma_paciente_cambio_si_o_no', 'tratamiento_medicacion_duracion', 'tratamiento_consulta_especialista_si_o_no', 'psiquiatria', 'afirmar', 'sintoma_paciente_seguimiento_describir', 'tratamiento_medicacion_antecedentes', 'tratamiento_medicacion_si_o_no', 'personal_dieta_describir', 'personal_trabajo_horas', 'personal_viajes_otros', 'tratamiento_diagnostico_quien', 'sintoma_paciente_embarazo_fin']
le = LabelEncoder()
le.fit(target)
target_num = le.transform(target)

def clean_text(text):
    # letra xehera
    text = text.lower()
    # puntuazioa kendu
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    # hurrengo lerroa ezabatu
    text = re.sub(r'[^ \w\.]', '', text)

    return text


class Actionpersonal_entorno_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_entorno_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
	
        if paciente == 1 : 
            respuesta = "Sí"
        elif paciente == 2:
            respuesta = "Sí"
        elif paciente == 3:
            respuesta = "Sí"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_medicacion_cuando_describir(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_cuando_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No he tomado ninguna medicación"
        elif paciente == 2:
            respuesta = "No he tomado ninguna medicación"
        elif paciente == 3:
            respuesta = "Me he tomado un paracetamol antes de venir"
	 
        dispatcher.utter_message(text=respuesta)

        return []

class Actiontratamiento_medicacion_cuando_si_o_no(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_cuando_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "Sí"
	 
        dispatcher.utter_message(text=respuesta)

        return []



class Actionafirmar(Action):

    def name(self) -> Text:
        return "action_afirmar"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Alguna pregunta más"
        elif paciente == 2:
            respuesta = "Alguna pregunta más"
        elif paciente == 3:
            respuesta = "Alguna pregunta más"
	 
        dispatcher.utter_message(text=respuesta)


        return []


class Actiondespedida(Action):

    def name(self) -> Text:
        return "action_despedida"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Agur"
        elif paciente == 2:
            respuesta = "Adiós"
        elif paciente == 3:
            respuesta = "Agur. Eskerrik asko"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionestado(Action):

    def name(self) -> Text:
        return "action_estado"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Muy mal"
        elif paciente == 2:
            respuesta = "No puedo mas del dolor"
        elif paciente == 3:
            respuesta = "Regular"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionmotivo_de_consulta(Action):

    def name(self) -> Text:
        return "action_motivo_de_consulta"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Me duele al respirar y me duele el pecho"
        elif paciente == 2:
            respuesta = "Me duele todo el cuerpo y tengo la mano negra"
        elif paciente == 3:
            respuesta = "Tengo tos y mocos"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionotros(Action):

    def name(self) -> Text:
        return "action_otros"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Me parece bien"
        elif paciente == 2:
            respuesta = "De acuerdo"
        elif paciente == 3:
            respuesta = "Perfecto"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_alcohol_cantidad(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_alcohol_cantidad"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        if paciente == 1 : 
            respuesta = "No bebo alcohol"
        elif paciente == 2:
            respuesta = "No bebo alcohol"
        elif paciente == 3:
            respuesta = "No bebo alcohol"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_alcohol_describir(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_alcohol_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No bebo alcohol"
        elif paciente == 2:
            respuesta = "No bebo alcohol"
        elif paciente == 3:
            respuesta = "No bebo alcohol"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_alcohol_duracion(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_alcohol_duracion"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No bebo alcohol"
        elif paciente == 2:
            respuesta = "No bebo alcohol"
        elif paciente == 3:
            respuesta = "No bebo alcohol"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_alcohol_frecuencia(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_alcohol_frecuencia"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No bebo alcohol"
        elif paciente == 2:
            respuesta = "No bebo alcohol"
        elif paciente == 3:
            respuesta = "No bebo alcohol"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_alcohol_otros(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_alcohol_otros"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No bebo alcohol"
        elif paciente == 2:
            respuesta = "No bebo alcohol"
        elif paciente == 3:
            respuesta = "No bebo alcohol"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_alcohol_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_alcohol_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "No"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_fumar_cantidad(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_fumar_cantidad"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Fumo bastante tabaco"
        elif paciente == 2:
            respuesta = "No fumo"
        elif paciente == 3:
            respuesta = "No fumo"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_fumar_duracion(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_fumar_duracion"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Llevo fumando 10 años"
        elif paciente == 2:
            respuesta = "No fumo"
        elif paciente == 3:
            respuesta = "No fumo"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_fumar_frecuencia(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_fumar_frecuencia"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Fumo 2 paquetes de tabaco todos los dias"
        elif paciente == 2:
            respuesta = "No fumo"
        elif paciente == 3:
            respuesta = "No fumo"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_fumar_inicio(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_fumar_inicio"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Empece a fumar en 2013"
        elif paciente == 2:
            respuesta = "No fumo"
        elif paciente == 3:
            respuesta = "No fumo"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_fumar_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_fumar_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Sí"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "No"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_otros_describir(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_otros_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Mi única adiccion es fumar"
        elif paciente == 2:
            respuesta = "No tengo ninguna adicción"
        elif paciente == 3:
            respuesta = "No tengo ninguna adicción"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_adiccion_otros_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_adiccion_otros_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Mi única adiccion es fumar"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "No"
	 
        dispatcher.utter_message(text=respuesta)


        return []


class Actionpersonal_contacto(Action):

    def name(self) -> Text:
        return "action_personal_contacto"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Mi novia es mi persona de contacto"
        elif paciente == 2:
            respuesta = "Mi madre es mi persona de contacto"
        elif paciente == 3:
            respuesta = "Mi abuela es con la que tienes que contactar"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_datos_direccion(Action):

    def name(self) -> Text:
        return "action_personal_datos_direccion"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Vivo en Lekeitio"
        elif paciente == 2:
            respuesta = "Vivo en Bilbao"
        elif paciente == 3:
            respuesta = "Vivo en Gasteiz"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_datos_edad(Action):

    def name(self) -> Text:
        return "action_personal_datos_edad"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Tengo 50 años"
        elif paciente == 2:
            respuesta = "Tengo 30 años"
        elif paciente == 3:
            respuesta = "Tengo 44 años"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_datos_fecha_de_nacimiento(Action):

    def name(self) -> Text:
        return "action_personal_datos_fecha_de_nacimiento"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "nací el 1 de noviembre del 72"
        elif paciente == 2:
            respuesta = "soy del 16 de junio del 92"
        elif paciente == 3:
            respuesta = "nací en mayo del 78"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_datos_nombre(Action):

    def name(self) -> Text:
        return "action_personal_datos_nombre"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Me llamo Mikel"
        elif paciente == 2:
            respuesta = "Soy Janire"
        elif paciente == 3:
            respuesta = "Me llamo Maitane"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_deporte_cantidad(Action):

    def name(self) -> Text:
        return "action_personal_deporte_cantidad"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Hago algo de deporte"
        elif paciente == 2:
            respuesta = "No hago nada de deporte"
        elif paciente == 3:
            respuesta = "Hago mucho deporte"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_deporte_cuando(Action):

    def name(self) -> Text:
        return "action_personal_deporte_cuando"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "La última vez que hice deporte fue la semana pasada"
        elif paciente == 2:
            respuesta = "No hago nada de deporte"
        elif paciente == 3:
            respuesta = "Ayer hice por última vez deporte"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_deporte_describir(Action):

    def name(self) -> Text:
        return "action_personal_deporte_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Hago Judo"
        elif paciente == 2:
            respuesta = "No hago nada de deporte"
        elif paciente == 3:
            respuesta = "Hago volley ball y judo"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_deporte_frecuencia(Action):

    def name(self) -> Text:
        return "action_personal_deporte_frecuencia"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Hago deporte una vez a la semana"
        elif paciente == 2:
            respuesta = "No hago nada de deporte"
        elif paciente == 3:
            respuesta = "Los sabados es mi único dia de descanso"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_deporte_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_deporte_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Sí"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "Sí"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_dieta_cantidad(Action):

    def name(self) -> Text:
        return "action_personal_dieta_cantidad"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Como muchisima cantidad de comida"
        elif paciente == 2:
            respuesta = "Apenas como"
        elif paciente == 3:
            respuesta = "Como muy poco"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_dieta_cuando(Action):

    def name(self) -> Text:
        return "action_personal_dieta_cuando"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "He comido hace una hora"
        elif paciente == 2:
            respuesta = "Llevo sin comer 2 días"
        elif paciente == 3:
            respuesta = "He comido antes de venir"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_dieta_describir(Action):

    def name(self) -> Text:
        return "action_personal_dieta_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Me alimento a base de hamburguesas"
        elif paciente == 2:
            respuesta = "Solo como chucherias"
        elif paciente == 3:
            respuesta = "Tengo una dieta variada y nutritiva"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_dieta_duracion(Action):

    def name(self) -> Text:
        return "action_personal_dieta_duracion"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Llevo así 10 años"
        elif paciente == 2:
            respuesta = "He comido así durante 5 años"
        elif paciente == 3:
            respuesta = "Toda mi vida he llevado esta dieta"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_dieta_frecuencia(Action):

    def name(self) -> Text:
        return "action_personal_dieta_frecuencia"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Todos los días" 
        elif paciente == 2:
            respuesta = "Todos los días"
        elif paciente == 3:
            respuesta = "Casi siempre"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_dieta_otros(Action):

    def name(self) -> Text:
        return "action_personal_dieta_otros"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No hecomido nada fuera de lo común" 
        elif paciente == 2:
            respuesta = "No hecomido nada fuera de lo común"
        elif paciente == 3:
            respuesta = "No hecomido nada fuera de lo común"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_dieta_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_dieta_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        if paciente == 1 : 
            respuesta = "No" 
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "Sí"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_describir(Action):

    def name(self) -> Text:
        return "action_personal_entorno_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Me rodeo de mucha gente" 
        elif paciente == 2:
            respuesta = "Me encanta estar con gente"
        elif paciente == 3:
            respuesta = "Quedo con gente a diario"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_hijos_describir(Action):

    def name(self) -> Text:
        return "action_personal_entorno_hijos_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No tengo hijos" 
        elif paciente == 2:
            respuesta = "No tengo hijos"
        elif paciente == 3:
            respuesta = "Tengo 2 hijas"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_hijos_edad(Action):

    def name(self) -> Text:
        return "action_personal_entorno_hijos_edad"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No tengo hijos" 
        elif paciente == 2:
            respuesta = "No tengo hijos"
        elif paciente == 3:
            respuesta = "Tienen 14 años mis 2 hijas"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_hijos_nombre(Action):

    def name(self) -> Text:
        return "action_personal_entorno_hijos_nombre"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No tengo hijos" 
        elif paciente == 2:
            respuesta = "No tengo hijos"
        elif paciente == 3:
            respuesta = "Una se llama Cloe y la otra Lara"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_hijos_otros(Action):

    def name(self) -> Text:
        return "action_personal_entorno_hijos_otros"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No tengo hijos" 
        elif paciente == 2:
            respuesta = "No tengo hijos"
        elif paciente == 3:
            respuesta = "Estan ahora mismo yendo a la escuela"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_hijos_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_entorno_hijos_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No" 
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "Sí"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_mascota_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_entorno_mascota_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No" 
        elif paciente == 2:
            respuesta = "Sí"
        elif paciente == 3:
            respuesta = "No"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_otros_describir(Action):

    def name(self) -> Text:
        return "action_personal_entorno_otros_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Vivo con mi pareja" 
        elif paciente == 2:
            respuesta = "Vivo con mi pareja"
        elif paciente == 3:
            respuesta = "Vivo con mi pareja, hijas y mascota"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_otros_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_entorno_otros_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Sí" 
        elif paciente == 2:
            respuesta = "Sí"
        elif paciente == 3:
            respuesta = "Sí"
	 
        dispatcher.utter_message(text=respuesta)


        return []


class Actionpersonal_entorno_padres_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_entorno_padres_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Sí" 
        elif paciente == 2:
            respuesta = "Sí"
        elif paciente == 3:
            respuesta = "Sí"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_pareja_nombre(Action):

    def name(self) -> Text:
        return "action_personal_entorno_pareja_nombre"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "El nombre de mi pareja es Maite" 
        elif paciente == 2:
            respuesta = "El nombre de mi pareja es Yeray"
        elif paciente == 3:
            respuesta = "El nombre de mi pareja es Julia"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_pareja_otros(Action):

    def name(self) -> Text:
        return "action_personal_entorno_pareja_otros"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Muy bien"  
        elif paciente == 2:
            respuesta = "Muy bien"
        elif paciente == 3:
            respuesta = "Muy bien"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_entorno_pareja_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_entorno_pareja_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Sí"  
        elif paciente == 2:
            respuesta = "Sí"
        elif paciente == 3:
            respuesta = "Sí"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_fisico_altura(Action):

    def name(self) -> Text:
        return "action_personal_fisico_altura"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Mido 1,77 metros"  
        elif paciente == 2:
            respuesta = "Mido 1,55 metros"
        elif paciente == 3:
            respuesta = "Con plataformas mido 1,78 metros"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_fisico_peso_cambio(Action):

    def name(self) -> Text:
        return "action_personal_fisico_peso_cambio"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Mido 1,77 metros"  
        elif paciente == 2:
            respuesta = "Mido 1,55 metros"
        elif paciente == 3:
            respuesta = "Con plataformas mido 1,78 metros"
	 
        dispatcher.utter_message(text=respuesta)


        return []


class Actionpersonal_fisico_peso_duracion(Action):

    def name(self) -> Text:
        return "action_personal_fisico_peso_duracion"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Llevo con 90 kilos un año"  
        elif paciente == 2:
            respuesta = "Llevo con 55 kilos 10 años"
        elif paciente == 3:
            respuesta = "Llevo con 64 kilos dos años"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_fisico_peso_peso(Action):

    def name(self) -> Text:
        return "action_personal_fisico_peso_peso"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Peso 90 kilos"  
        elif paciente == 2:
            respuesta = "Peso 55 kilos"
        elif paciente == 3:
            respuesta = "Peso 64 kilos"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_otros_describir(Action):

    def name(self) -> Text:
        return "action_personal_otros_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Me gusta pasear"  
        elif paciente == 2:
            respuesta = "Me gusta jugar a video juegos"
        elif paciente == 3:
            respuesta = "Me gusta hacer deporte"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_otros_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_otros_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No me apetece responder a esa pregunta"  
        elif paciente == 2:
            respuesta = "No me apetece responder a esa pregunta"
        elif paciente == 3:
            respuesta = "No me apetece responder a esa pregunta"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_sueño_describir(Action):

    def name(self) -> Text:
        return "action_personal_sueño_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Últimamente me cuesta mucho dormir"  
        elif paciente == 2:
            respuesta = "Tengo sueño interminetente nunca termino de dormir por el dolor"
        elif paciente == 3:
            respuesta = "Duermo como un tronco"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_sueño_horas(Action):

    def name(self) -> Text:
        return "action_personal_sueño_horas"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Duermo solo 1 hora"  
        elif paciente == 2:
            respuesta = "Duermo solo 3 horas al día"
        elif paciente == 3:
            respuesta = "Duermo mis 8 horas como es debido"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_sueño_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_sueño_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"  
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "Sí"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_trabajo_anterior(Action):

    def name(self) -> Text:
        return "action_personal_trabajo_anterior"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Solo he trabajado de profesor"  
        elif paciente == 2:
            respuesta = "Trabaje en una consultoría"
        elif paciente == 3:
            respuesta = "Trabaje de panadera una época"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_trabajo_describir(Action):

    def name(self) -> Text:
        return "action_personal_trabajo_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Soy profesor"  
        elif paciente == 2:
            respuesta = "Soy profesora"
        elif paciente == 3:
            respuesta = "Trabajo de hacker"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_trabajo_duracion(Action):

    def name(self) -> Text:
        return "action_personal_trabajo_duracion"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Llevo toda la vida de profesor"  
        elif paciente == 2:
            respuesta = "Llevo 3 años de profesora"
        elif paciente == 3:
            respuesta = "Trabajo desde los 20 de hacker"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_trabajo_horas(Action):

    def name(self) -> Text:
        return "action_personal_trabajo_horas"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Trabajo 8 horas"  
        elif paciente == 2:
            respuesta = "Trabajo 8 horas"
        elif paciente == 3:
            respuesta = "Trabajo 24 horas"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_trabajo_lugar(Action):

    def name(self) -> Text:
        return "action_personal_trabajo_lugar"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Trabajo en la universidad del país vasco"  
        elif paciente == 2:
            respuesta = "Trabajo en la universidad del país vasco"
        elif paciente == 3:
            respuesta = "Trabajo en españa de hacker"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_trabajo_otros(Action):

    def name(self) -> Text:
        return "action_personal_trabajo_otros"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Muy bien"  
        elif paciente == 2:
            respuesta = "Muy bien"
        elif paciente == 3:
            respuesta = "Muy bien"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_trabajo_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_trabajo_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Sí"  
        elif paciente == 2:
            respuesta = "Sí"
        elif paciente == 3:
            respuesta = "Sí"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_viajes_describir(Action):

    def name(self) -> Text:
        return "action_personal_viajes_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No he salido de casa últimamente"
        elif paciente == 2:
            respuesta = "He ido a Australia"
        elif paciente == 3:
            respuesta = "No me he movido de mi provincia en los últimos años"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_viajes_otros(Action):

    def name(self) -> Text:
        return "action_personal_viajes_otros"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Voy a vivir en España por el resto de mi vida"
        elif paciente == 2:
            respuesta = "Voy a vivir en España por el resto de mi vida"
        elif paciente == 3:
            respuesta = "Voy a vivir en España por el resto de mi vida"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpersonal_viajes_si_o_no(Action):

    def name(self) -> Text:
        return "action_personal_viajes_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "Sí"
        elif paciente == 3:
            respuesta = "No"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpsiquiatria(Action):

    def name(self) -> Text:
        return "action_psiquiatria"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Me suelo encontrar muy feliz"
        elif paciente == 2:
            respuesta = "Soy una persona feliz"
        elif paciente == 3:
            respuesta = "Soy muy feliz"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpsiquiatria_estado_de_animo_describir(Action):

    def name(self) -> Text:
        return "action_psiquiatria_estado_de_animo_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "A veces me encuentro estresado" 
        elif paciente == 2:
            respuesta = "A veces me encuentro triste"
        elif paciente == 3:
            respuesta = "A veces me encuentro estresada"
	 
        dispatcher.utter_message(text=respuesta)

        return []


class Actionpsiquiatria_estado_de_animo_si_o_no(Action):

    def name(self) -> Text:
        return "action_psiquiatria_estado_de_animo_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Sí" 
        elif paciente == 2:
            respuesta = "Sí"
        elif paciente == 3:
            respuesta = "Sí"
	 
        dispatcher.utter_message(text=respuesta)


        return []


class Actionsaludo(Action):

    def name(self) -> Text:
        return "action_saludo"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Hola"
        elif paciente == 2:
            respuesta = "Buenas"
        elif paciente == 3:
            respuesta = "Hey"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_bebe_peso(Action):

    def name(self) -> Text:
        return "action_sintoma_bebe_peso"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No tengo bebes"
        elif paciente == 2:
            respuesta = "No tengo bebes"
        elif paciente == 3:
            respuesta = "No tengo bebes"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_bebe_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_bebe_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No tengo bebes"
        elif paciente == 2:
            respuesta = "No tengo bebes"
        elif paciente == 3:
            respuesta = "No tengo bebes"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actionsintoma_entorno_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_entorno_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No tengo bebes"
        elif paciente == 2:
            respuesta = "No tengo bebes"
        elif paciente == 3:
            respuesta = "No tengo bebes"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_familia_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_familia_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Nadie en mi familia ha tenido un problema parecido"
        elif paciente == 2:
            respuesta = "Nadie en mi familia ha tenido un problema parecido"
        elif paciente == 3:
            respuesta = "Nadie en mi familia ha tenido un problema parecido"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_familia_inicio(Action):

    def name(self) -> Text:
        return "action_sintoma_familia_inicio"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Nadie en mi familia ha tenido un problema parecido"
        elif paciente == 2:
            respuesta = "Nadie en mi familia ha tenido un problema parecido"
        elif paciente == 3:
            respuesta = "Nadie en mi familia ha tenido un problema parecido"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actionsintoma_familia_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_familia_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "No"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_alergia_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_alergia_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No tengo ninguna alergia"
        elif paciente == 2:
            respuesta = "No tengo ninguna alergia"
        elif paciente == 3:
            respuesta = "Tengo alergia a la plata"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_alergia_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_alergia_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "Solo tengo alergia a la plata"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_antecedentes_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_antecedentes_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No tengo ningún antecedente"
        elif paciente == 2:
            respuesta = "No tengo ningún antecedente"
        elif paciente == 3:
            respuesta = "No tengo ningún antecedente"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_antecedentes_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_antecedentes_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "No"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_aparicion_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_aparicion_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "El problema aparecío hace una semana"
        elif paciente == 2:
            respuesta = "El problema aparecío hace una cuando volvi de Australia"
        elif paciente == 3:
            respuesta = "El problema aparecío hace 2 días"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_aparicion_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_aparicion_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "El problema aparecío hace una semana"
        elif paciente == 2:
            respuesta = "El problema aparecío hace una cuando volvi de Australia después de que me mordiera una araña"
        elif paciente == 3:
            respuesta = "El problema aparecío hace 2 días"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actionsintoma_paciente_cambio_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_cambio_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "El dolor no se alivia de ninguna manera"
        elif paciente == 2:
            respuesta = "El dolor no se alivia de ninguna manera"
        elif paciente == 3:
            respuesta = "No me duele nada"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_cambio_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_cambio_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "El dolor no se alivia de ninguna manera"
        elif paciente == 2:
            respuesta = "El dolor no se alivia de ninguna manera"
        elif paciente == 3:
            respuesta = "No me duele nada"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_capacidad_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_capacidad_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Me cuesta mucho hacer todo"
        elif paciente == 2:
            respuesta = "Me cuesta mucho hacer todo"
        elif paciente == 3:
            respuesta = "Soy capaz de hacer todo"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_capacidad_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_capacidad_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Me cuesta mucho hacer todo"
        elif paciente == 2:
            respuesta = "Me cuesta mucho hacer todo"
        elif paciente == 3:
            respuesta = "Soy capaz de hacer todo"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_causa_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_causa_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Creo que puede ser porque fumo mucho"
        elif paciente == 2:
            respuesta = "Creo que puede ser porque me pico la araña"
        elif paciente == 3:
            respuesta = "No se porque puede ser"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_causa_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_causa_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Creo que puede ser porque fumo mucho"
        elif paciente == 2:
            respuesta = "Creo que puede ser porque me pico la araña"
        elif paciente == 3:
            respuesta = "No se porque puede ser"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No puedo respirar, de vez en cuando escupo sangre y me duele mucho el pecho"
        elif paciente == 2:
            respuesta = "Tengo la mano negra y me duele todo el cuerpo"
        elif paciente == 3:
            respuesta = "Tengo tos y mocos"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_duracion(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_duracion"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "He estado asi durante una semana"
        elif paciente == 2:
            respuesta = "He estado asi desde que volvi de Australia"
        elif paciente == 3:
            respuesta = "He estado asi durante 3 días"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_embarazo_antecedentes(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_embarazo_antecedentes"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No he estado embarazado xd"
        elif paciente == 2:
            respuesta = "No he estado embarazada"
        elif paciente == 3:
            respuesta = "He estado embarazada hace 14 años"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_embarazo_cantidad(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_embarazo_cantidad"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No he estado embarazado xd"
        elif paciente == 2:
            respuesta = "No he estado embarazada"
        elif paciente == 3:
            respuesta = "Solo he estado embarazada una vez"


        dispatcher.utter_message(text=respuesta)


        return []


class Actionsintoma_paciente_embarazo_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_embarazo_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No he estado embarazado xd"
        elif paciente == 2:
            respuesta = "No he estado embarazada"
        elif paciente == 3:
            respuesta = "El embarazo fue muy bien"


        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_embarazo_fin(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_embarazo_fin"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No he estado embarazado xd"
        elif paciente == 2:
            respuesta = "No he estado embarazada"
        elif paciente == 3:
            respuesta = "Ya no estoy embarazada"


        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_embarazo_otros(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_embarazo_otros"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No he estado embarazado xd"
        elif paciente == 2:
            respuesta = "No he estado embarazada"
        elif paciente == 3:
            respuesta = "Ya no estoy embarazada, pero la anterio fue un embarazo normal de gemelas"


        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_embarazo_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_embarazo_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "No"


        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_fiebre_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_fiebre_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Tengo 39 grados de fiebre"
        elif paciente == 2:
            respuesta = "Tengo 41 grados de fiebre"
        elif paciente == 3:
            respuesta = "No tengo fiebre"


        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_fiebre_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_fiebre_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Sí"
        elif paciente == 2:
            respuesta = "Sí"
        elif paciente == 3:
            respuesta = "No"


        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_frecuencia(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_frecuencia"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Todo el rato"
        elif paciente == 2:
            respuesta = "Todo el rato"
        elif paciente == 3:
            respuesta = "De vez en cuando"


        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_inicio(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_inicio"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "He estado asi durante una semana"
        elif paciente == 2:
            respuesta = "He estado asi desde que volvi de Australia"
        elif paciente == 3:
            respuesta = "He estado asi durante 3 días"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_localizacion_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_localizacion_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Me duele mucho el pecho"
        elif paciente == 2:
            respuesta = "Me duele todo, pero sobretodo la mano"
        elif paciente == 3:
            respuesta = "No me duele nada"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_localizacion_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_localizacion_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        if paciente == 1 : 
            respuesta = "Me duele mucho el pecho"
        elif paciente == 2:
            respuesta = "Me duele todo, pero sobretodo la mano"
        elif paciente == 3:
            respuesta = "No me duele nada"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actionsintoma_paciente_secuela_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_secuela_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No me deja trabajar"
        elif paciente == 2:
            respuesta = "No puedo trabajar"
        elif paciente == 3:
            respuesta = "No me deja ninguna secuela"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_secuela_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_secuela_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        if paciente == 1 : 
            respuesta = "No me deja trabajar"
        elif paciente == 2:
            respuesta = "No puedo trabajar"
        elif paciente == 3:
            respuesta = "No me deja ninguna secuela"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_seguimiento_describir(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_seguimiento_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No se me ha hecho ningún seguimiento"
        elif paciente == 2:
            respuesta = "No se me ha hecho ningún seguimiento"
        elif paciente == 3:
            respuesta = "No se me ha hecho ningún seguimiento"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_seguimiento_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_seguimiento_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "No"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionsintoma_paciente_si_o_no(Action):

    def name(self) -> Text:
        return "action_sintoma_paciente_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Solo no puedo respirar, de vez en cuando escupo sangre y me duele mucho el pecho"
        elif paciente == 2:
            respuesta = "Solo tengo la mano negra y me duele todo el cuerpo"
        elif paciente == 3:
            respuesta = "Solo tengo tos y mocos"


	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_anticonceptivos_describir(Action):

    def name(self) -> Text:
        return "action_tratamiento_anticonceptivos_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Creo que no tiene que ver con mi enfermedad"
        elif paciente == 2:
            respuesta = "Creo que no tiene que ver con mi enfermedad"
        elif paciente == 3:
            respuesta = "Creo que no tiene que ver con mi enfermedad"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_anticonceptivos_frecuencia(Action):

    def name(self) -> Text:
        return "action_tratamiento_anticonceptivos_frecuencia"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Los usamos cada vez que practicamos relaciones sexuales"
        elif paciente == 2:
            respuesta = "Los usamos cada vez que practicamos relaciones sexuales"
        elif paciente == 3:
            respuesta = "Los usamos cada vez que practicamos relaciones sexuales"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_anticonceptivos_si_o_no(Action):

    def name(self) -> Text:
        return "action_tratamiento_anticonceptivos_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Sí"
        elif paciente == 2:
            respuesta = "Sí"
        elif paciente == 3:
            respuesta = "Sí"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_consulta_describir(Action):

    def name(self) -> Text:
        return "action_tratamiento_consulta_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No he tenido ninguna otra consulta"
        elif paciente == 2:
            respuesta = "No he tenido ninguna otra consulta"
        elif paciente == 3:
            respuesta = "No he tenido ninguna otra consulta"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actiontratamiento_consulta_especialista_si_o_no(Action):

    def name(self) -> Text:
        return "action_tratamiento_consulta_especialista_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "No"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actiontratamiento_consulta_fecha(Action):

    def name(self) -> Text:
        return "action_tratamiento_consulta_fecha"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No he tenido ninguna otra consulta"
        elif paciente == 2:
            respuesta = "No he tenido ninguna otra consulta"
        elif paciente == 3:
            respuesta = "No he tenido ninguna otra consulta"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actiontratamiento_consulta_si_o_no(Action):

    def name(self) -> Text:
        return "action_tratamiento_consulta_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "No"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actiontratamiento_diagnostico_como(Action):

    def name(self) -> Text:
        return "action_tratamiento_diagnostico_como"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No sé que tengo"
        elif paciente == 2:
            respuesta = "No sé que tengo"
        elif paciente == 3:
            respuesta = "No sé que tengo"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actiontratamiento_diagnostico_fecha(Action):

    def name(self) -> Text:
        return "action_tratamiento_diagnostico_fecha"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No he tenido ningún diagnostico"
        elif paciente == 2:
            respuesta = "No he tenido ningún diagnostico"
        elif paciente == 3:
            respuesta = "No he tenido ningún diagnostico"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actiontratamiento_diagnostico_quien(Action):

    def name(self) -> Text:
        return "action_tratamiento_diagnostico_quien"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No he tenido ningún diagnostico"
        elif paciente == 2:
            respuesta = "No he tenido ningún diagnostico"
        elif paciente == 3:
            respuesta = "No he tenido ningún diagnostico"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_diagnostico_si_o_no(Action):

    def name(self) -> Text:
        return "action_tratamiento_diagnostico_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "No"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_historial_describir(Action):

    def name(self) -> Text:
        return "action_tratamiento_historial_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No tengo ningún historial"
        elif paciente == 2:
            respuesta = "No tengo ningún historial"
        elif paciente == 3:
            respuesta = "No tengo ningún historial"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_historial_si_o_no(Action):

    def name(self) -> Text:
        return "action_tratamiento_historial_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "No"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_medicacion_antecedentes(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_antecedentes"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No me han recetado nada antes"
        elif paciente == 2:
            respuesta = "No me han recetado nada antes"
        elif paciente == 3:
            respuesta = "No me han recetado nada antes"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_medicacion_cuando(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_cuando"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        if paciente == 1 : 
            respuesta = "No me han recetado nada antes"
        elif paciente == 2:
            respuesta = "No me han recetado nada antes"
        elif paciente == 3:
            respuesta = "Me he tomado un paracetamol antes de venir"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actiontratamiento_medicacion_describir(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No me he medicado"
        elif paciente == 2:
            respuesta = "No me he medicado"
        elif paciente == 3:
            respuesta = "Me he tomado un paracetamol antes de venir"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_medicacion_dosis(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_dosis"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No me he medicado"
        elif paciente == 2:
            respuesta = "No me he medicado"
        elif paciente == 3:
            respuesta = "Solo me he tomado una pastilla de paracetamol"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_medicacion_duracion(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_duracion"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No me he medicado"
        elif paciente == 2:
            respuesta = "No me he medicado"
        elif paciente == 3:
            respuesta = "Solo me he tomado una pastilla de paracetamol"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_medicacion_frecuencia(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_frecuencia"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No me he medicado"
        elif paciente == 2:
            respuesta = "No me he medicado"
        elif paciente == 3:
            respuesta = "Solo me he tomado una pastilla de paracetamol antes de venir"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actiontratamiento_medicacion_motivo(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_motivo"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No me he medicado"
        elif paciente == 2:
            respuesta = "No me he medicado"
        elif paciente == 3:
            respuesta = "Para a ver si me quitaba la tos"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_medicacion_otros(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_otros"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No me he medicado"
        elif paciente == 2:
            respuesta = "No me he medicado"
        elif paciente == 3:
            respuesta = "Para a ver si me quitaba la tos"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_medicacion_receta(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_receta"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Vale"
        elif paciente == 2:
            respuesta = "Vale"
        elif paciente == 3:
            respuesta = "Vale"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_medicacion_si_o_no(Action):

    def name(self) -> Text:
        return "action_tratamiento_medicacion_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "No"
        elif paciente == 2:
            respuesta = "No"
        elif paciente == 3:
            respuesta = "Solo me he tomado una pastilla de paracetamol antes de venir"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_operacion_complicaciones(Action):

    def name(self) -> Text:
        return "action_tratamiento_operacion_complicaciones"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Nunca me he operado"
        elif paciente == 2:
            respuesta = "Nunca me he operado"
        elif paciente == 3:
            respuesta = "Nunca me he operado"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_operacion_describir(Action):

    def name(self) -> Text:
        return "action_tratamiento_operacion_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Nunca me he operado"
        elif paciente == 2:
            respuesta = "Nunca me he operado"
        elif paciente == 3:
            respuesta = "Nunca me he operado"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_operacion_dosis(Action):

    def name(self) -> Text:
        return "action_tratamiento_operacion_dosis"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Nunca me he operado"
        elif paciente == 2:
            respuesta = "Nunca me he operado"
        elif paciente == 3:
            respuesta = "Nunca me he operado"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_operacion_especialista(Action):

    def name(self) -> Text:
        return "action_tratamiento_operacion_especialista"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Nunca me he operado"
        elif paciente == 2:
            respuesta = "Nunca me he operado"
        elif paciente == 3:
            respuesta = "Nunca me he operado"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_operacion_fecha(Action):

    def name(self) -> Text:
        return "action_tratamiento_operacion_fecha"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Nunca me he operado"
        elif paciente == 2:
            respuesta = "Nunca me he operado"
        elif paciente == 3:
            respuesta = "Nunca me he operado"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_operacion_frecuencia(Action):

    def name(self) -> Text:
        return "action_tratamiento_operacion_frecuencia"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Nunca me he operado"
        elif paciente == 2:
            respuesta = "Nunca me he operado"
        elif paciente == 3:
            respuesta = "Nunca me he operado"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_operacion_motivo(Action):

    def name(self) -> Text:
        return "action_tratamiento_operacion_motivo"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Nunca me he operado"
        elif paciente == 2:
            respuesta = "Nunca me he operado"
        elif paciente == 3:
            respuesta = "Nunca me he operado"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_operacion_resultados(Action):

    def name(self) -> Text:
        return "action_tratamiento_operacion_resultados"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Nunca me he operado"
        elif paciente == 2:
            respuesta = "Nunca me he operado"
        elif paciente == 3:
            respuesta = "Nunca me he operado"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actiontratamiento_operacion_si_o_no(Action):

    def name(self) -> Text:
        return "action_tratamiento_operacion_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Nunca me he operado"
        elif paciente == 2:
            respuesta = "Nunca me he operado"
        elif paciente == 3:
            respuesta = "Nunca me he operado"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionvida_sexual_describir(Action):

    def name(self) -> Text:
        return "action_vida_sexual_describir"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Tenemos una vida sexual muy normalita"
        elif paciente == 2:
            respuesta = "Tenemos una vida sexual muy normalita"
        elif paciente == 3:
            respuesta = "Tenemos una vida sexual muy normalita"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionvida_sexual_edad(Action):

    def name(self) -> Text:
        return "action_vida_sexual_edad"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Prefiero no responder a esa pregunta"
        elif paciente == 2:
            respuesta = "Prefiero no responder a esa pregunta"
        elif paciente == 3:
            respuesta = "Prefiero no responder a esa pregunta"
	
        dispatcher.utter_message(text=respuesta)


        return []


class Actionvida_sexual_frecuencia(Action):

    def name(self) -> Text:
        return "action_vida_sexual_frecuencia"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Prefiero no responder a esa pregunta"
        elif paciente == 2:
            respuesta = "Prefiero no responder a esa pregunta"
        elif paciente == 3:
            respuesta = "Prefiero no responder a esa pregunta"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionvida_sexual_otros(Action):

    def name(self) -> Text:
        return "action_vida_sexual_otros"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Prefiero no responder a esa pregunta"
        elif paciente == 2:
            respuesta = "Prefiero no responder a esa pregunta"
        elif paciente == 3:
            respuesta = "Prefiero no responder a esa pregunta"
	
        dispatcher.utter_message(text=respuesta)

        return []


class Actionvida_sexual_si_o_no(Action):

    def name(self) -> Text:
        return "action_vida_sexual_si_o_no"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if paciente == 1 : 
            respuesta = "Prefiero no responder a esa pregunta"
        elif paciente == 2:
            respuesta = "Prefiero no responder a esa pregunta"
        elif paciente == 3:
            respuesta = "Prefiero no responder a esa pregunta"
	
        dispatcher.utter_message(text=respuesta)

        return []

class Action_fallback(Action):

    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = clean_text(tracker.latest_message['text'])
        sol = pipe(text)
        prediction = le.inverse_transform([int(sol[0]["label"].split("_")[1])])


        return [FollowupAction("action_"+prediction[0])]



