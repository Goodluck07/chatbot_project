# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#

import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideGreeting(Action):
    def name(self) -> Text:
        return "action_provide_greeting"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        selected_greeting = "Hey, nice to meet you!"
        dispatcher.utter_message(selected_greeting)
        return []

class ActionProvideMusicRecommendation(Action):
    def name(self) -> Text:
        return "action_provide_music_recommendation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recommendations = [
            "Bohemian Rhapsody - Queen",
            "Hotel California - Eagles",
            "Smells Like Teen Spirit - Nirvana",
            "Shape of You - Ed Sheeran",
            "Dance Monkey - Tones and I",
            "Blinding Lights - The Weeknd",
            "Stairway to Heaven - Led Zeppelin",
            "Rolling in the Deep - Adele",
            "Uptown Funk - Mark Ronson ft. Bruno Mars"
        ]
        selected_recommendations = random.sample(recommendations, 3)  # Select 3 random songs
        dispatcher.utter_message(f"Here are some songs for you: {', '.join(selected_recommendations)}")
        
        return []

    
class ExtractFoodEntity(Action):

    def name(self) -> Text:
        return "action_extract_food_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food_entity = next(tracker.get_latest_entity_values("food"), None)

        if food_entity:
            dispatcher.utter_message(text=f"You have selected {food_entity} as your food choice")
        else:
            dispatcher.utter_message(text = "I'm sorry, I could not detect the food choice")

        return []
    
class OrderFoodAction(Action):
    def name(self) -> Text:
        return "action_order_food"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sure, which kind of food would you like to order")

        return []
    
class ConfirmedOrderAction(Action):
    def name(self) -> Text:
        return "action_confirm_order"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        food_entity = next(tracker.get_latest_entity_values("food"), None)

        if food_entity:
            dispatcher.utter_message(text=f"I have ordered {food_entity} for you")
        else:
            dispatcher.utter_message(text = "I'm sorry, I could not confirm your order")

        return []