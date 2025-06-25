from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from logger import logger

class ActionOrderFood(Action):
    def name(self) -> Text:
        return "action_order_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food_item = tracker.get_slot("food_item")
        quantity = tracker.get_slot("quantity")

        if not food_item:
            dispatcher.utter_message(text="Please tell me what food item you'd like.")
            logger.warning("Missing slot: food_item")
        elif not quantity:
            dispatcher.utter_message(text="Please tell me how many you'd like.")
            logger.warning("Missing slot: quantity")
        else:
            dispatcher.utter_message(text=f"Order confirmed: {quantity} x {food_item}. Thank you!")
            logger.info(f"Order confirmed: {quantity} x {food_item}")

        return []

class ActionCancelOrder(Action):
    def name(self) -> Text:
        return "action_cancel_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your order has been cancelled.")
        logger.info("Order cancelled by user.")
        return []

class ActionBookTable(Action):
    def name(self) -> Text:
        return "action_book_table"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        guests = tracker.get_slot("number_of_guests")
        time = tracker.get_slot("reservation_time")

        if not guests or not time:
            dispatcher.utter_message(text="Please provide number of guests and reservation time.")
            logger.warning("Missing slot: number_of_guests or reservation_time")
        else:
            dispatcher.utter_message(text=f"Table booked for {guests} guests at {time}.")
            logger.info(f"Table booked for {guests} guests at {time}")

        return []

class ActionExtractSlots(Action):
    def name(self) -> Text:
        return "action_extract_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        logger.info("Extracting slots...")
        for slot_name in ["food_item", "quantity", "number_of_guests", "reservation_time"]:
            slot_value = tracker.get_slot(slot_name)
            logger.info(f"{slot_name}: {slot_value}")

        dispatcher.utter_message(text="Slots extracted for debugging.")
        return []