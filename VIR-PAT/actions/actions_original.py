# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd
import re
from googletrans import Translator

import spacy
from spacy.matcher import Matcher
import es_core_news_sm 
from spacy import displacy 
import visualise_spacy_tree

from IPython.display import Image, display
import es_core_news_sm
import os




def text2int (textnum, numwords={}):
	if not numwords:
		units = [
		"cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho",
		"nueve", "diez", "once", "doce", "trece", "catorce", "quince",
		"dieciséis", "diecisiete", "dieciocho", "diecinueve","veinte","veintiuno","veintidós","veintitrés","veinticuatro","veinticinco","veintiséis","veintisiete","veintiocho","veintinueve"
		]

		tens = ["", "", "", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa","cien"]

		scales = ["ciento", "mil", "millon"]

		numwords["y"] = (1, 0)
		for idx, word in enumerate(units):  numwords[word] = (1, idx)
		for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
		for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

	textnum = textnum.replace('-', ' ')

	current = result = 0
	curstring = ""
	onnumber = False
	for word in textnum.split():
		if word not in numwords:
			if onnumber:
				curstring += repr(result + current) + " "
			curstring += word + " "
			result = current = 0
			onnumber = False
		else:
			if word != "y":	
				scale, increment = numwords[word]
				current = current * scale + increment
				if scale > 100:
					result += current
					current = 0
				onnumber = True
			if word == "y" and onnumber:
				scale, increment = numwords[word]
				current = current * scale + increment
				if scale > 100:
					result += current
					current = 0
				onnumber = True
			if word == "y" and not onnumber:
				if onnumber:
					curstring += repr(result + current) + " "
				curstring += word + " "
				result = current = 0
				onnumber = False

	if onnumber:
		curstring += repr(result + current)

	return curstring

def _getText() -> Text:
	info = open("./actions/prueba.txt","r")
	text = info.read()
	info.close()
	return text2int(text)


# function to preprocess speech
def _clean(text) -> Text:
	# removing hyphens
	text = re.sub("-"," ",str(text))
	text = re.sub("— ","",str(text))
	# removing any reference to outside text
	text = re.sub("[\(\[].*?[\)\]]", "", str(text))

	return text

def _findAge(text) -> Text:
	nlp = spacy.load('es_core_news_sm',disable=['ner','textcat'])
	ages = []
	
	# spacy doc
	doc = nlp(text)

	# pattern DET + NOUN + ADP + NUM + años
	pattern_1 = [{'POS':'NOUN'},
		 {'POS':'ADP'},
		 {'POS':'NUM'},
		 {'LOWER': 'años'}]

	# pattern PROPN + ADP + NUM + años
	pattern_2 = [{'POS':'PROPN'},
		{'POS':'ADP'},
		{'POS':'NUM'},
		{'LOWER':'años'}]

	# pattern ADV + ADP + NUM + años
	pattern_3 = [{'POS':'ADV'},
		{'POS':'ADP'},
		{'POS':'NUM'},
		{'LOWER':'años'}]

	# pattern_4 = PROPN + ADV + ADJ + ADP + NUM + años
	pattern_4 = [{'POS':'PROPN'},
		 {'POS':'ADV'},
		 {'POS':'ADJ'},
		 {'POS':'ADP'},
		 {'POS':'NUM'},
		 {'LOWER':'años'}]

	# pattern_5 = DET + ADJ + ADP + NUM + años
	pattern_5 = [{'POS':'DET'},
		 {'POS':'ADJ'},
		 {'POS':'ADP'},
		 {'POS':'NUM'},
		 {'LOWER':'años'}]

	# pattern_6 = DET + NOUN + ADJ + ADP + NUM + años
	pattern_6 = [{'POS':'DET'},
		 {'POS':'NOUN'},
		 {'POS':'ADJ'},
		 {'POS':'ADP'},
		 {'POS':'NUM'},
		 {'LOWER':'años'}]

	# pattern_7 = NOUN + NUM + años
	pattern_7 = [{'POS':'NOUN'},
		 {'POS':'NUM'},
		 {'LOWER':'años'}]
		
	# Matcher class object 
	matcher = Matcher(nlp.vocab) 
	matcher.add("ages", [pattern_1, pattern_2 ,pattern_3, pattern_4, pattern_5, pattern_6, pattern_7]) 

	matches = matcher(doc)

	# finding patterns in the text
	for i in range(0,len(matches)):

		# match: id, start, end
		token = doc[matches[i][1]:matches[i][2]]
		# append token to list
		ages.append(str(token))
	    
	if ages != []:
		return ages[0]
	else:
		return ""

class ActionSintomas(Action):

	def name(self) -> Text:
		return "action_sintomas"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		#text = tracker.latest_message['text']
		translator = Translator() 
		info = _getText()

		dispatcher.utter_message(translator.translate(info , dest ='en').text)

		return []

class ActionFacilitySearch(Action):

	def name(self) -> Text:
		return "action_años"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

##		facility = tracker.get_slot("facility_type")
##		address = "Geometry Dash xd"
		info = _getText()
		text_clean = _clean(info)
		age = _findAge(text_clean)
		age_clean = re.sub("de ",'',str(age))
		age_clean_fin = " ".join(age_clean.split(" ")[-2:])
		if age_clean_fin == "":
			text="Prefiero no decirlo"
		else:
			text="Tengo {}".format(age_clean_fin)

		dispatcher.utter_message(text+str(kont))

		return []

class ActionFechaNacimiento(Action):

	def name(self) -> Text:
		return "action_fecha_nacimiento"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="He nacido en el 2000")

		return []

class ActionPeso(Action):

	def name(self) -> Text:
		return "action_peso"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Peso 100 kg")

		return []

class ActionAltura(Action):

	def name(self) -> Text:
		return "action_altura"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Mido 2,00 m")

		return []

class ActionFamilia(Action):

	def name(self) -> Text:
		return "action_familia"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Tengo 2 gatos")

		return []

class ActionHabitos(Action):

	def name(self) -> Text:
		return "action_habitos"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Me gusta comer mucho")

		return []

class ActionTrabajo(Action):

	def name(self) -> Text:
		return "action_trabajo"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Trabajo debajo de un puente")

		return []

class ActionDeporte(Action):

	def name(self) -> Text:
		return "action_deporte"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Practico el sofing")

		return []

class ActionSueño(Action):

	def name(self) -> Text:
		return "action_sueño"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Duermo entre 0 y 12 horas depende el día")

		return []

class ActionDieta(Action):

	def name(self) -> Text:
		return "action_dieta"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Solo como burguirs")

		return []

class ActionSintoma(Action):

	def name(self) -> Text:
		return "action_sintoma"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Tengo un sintoma")

		return []

class ActionTratamiento(Action):

	def name(self) -> Text:
		return "action_tratamiento"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Me llaman el ibuprofenos")

		return []

class ActionAntecedentesFamiliares(Action):

	def name(self) -> Text:
		return "action_antecedentes_familiares"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Mi familia ha sintomas")

		return []

class ActionFrecuenciaSintoma(Action):

	def name(self) -> Text:
		return "action_frecuencia_sintomas"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(text="Cada dia sufro el sintoma")

		return []





