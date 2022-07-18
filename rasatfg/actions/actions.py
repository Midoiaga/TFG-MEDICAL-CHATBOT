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

import spacy
from spacy.matcher import Matcher
import es_core_news_sm 
from spacy import displacy 
import visualise_spacy_tree

from IPython.display import Image, display
import es_core_news_sm
import os




def _getText() -> Text:
	info = open("./actions/prueba.txt","r")
	text = info.read()
	info.close()
	return text


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
		dispatcher.utter_message(text="Tengo {}".format(age_clean))

		return []
