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

	# pattern
	pattern = [{'POS':'ADP'},
	      {'POS':'NUM'},
	      {'LOWER':'años'}]
		
	# Matcher class object 
	matcher = Matcher(nlp.vocab) 
	matcher.add("ages", [pattern]) 

	matches = matcher(doc)

	# finding patterns in the text
	for i in range(0,len(matches)):

		# match: id, start, end
		token = doc[matches[i][1]:matches[i][2]]
		# append token to list
		ages.append(str(token))

	# # Only keep sentences containing Indian PMs
	# for age in ages:
	#     if (age.split()[2] == 'of') and (age.split()[3] != "India"):
	#             ages.remove(age)
	    
	return ages[0]


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
