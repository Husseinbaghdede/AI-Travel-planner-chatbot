from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itineary import generate_itineary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itineary = ""
        
        logger.info("Travel Planner initialized")
        
    def set_city(self,city):
        try:
           self.city = city
           self.messages.append(HumanMessage(content=city))
           logger.info(f"City set to {city}")
           
        except Exception as e:
            logger.error(f"Error setting city: {e}")
            raise CustomException(f"Error setting city". e)
    
    def set_interests(self,interests_str:str):
        try:
            
           self.interests = [i.strip() for i in interests_str.split(",")]
           self.messages.append(HumanMessage(content=interests_str))
           logger.info(f"Interests set sucesessfuly")
           
        except Exception as e:
            logger.error(f"Error setting interests: {e}")
            raise CustomException(f"Error setting interests", e)
           
    def create_itineary(self):
        try:
            logger.info(f"Generating itinerary for {self.city} and for interests {self.interests}")
            itineary = generate_itineary(self.city,self.interests)
            self.itineary = itineary   
            
            self.messages.append(AIMessage(content=itineary))
            logger.info(f"Itinerary generated successfully")
            return self.itineary
        except Exception as e:
            logger.error(f"Error generating itinerary: {e}")
            raise CustomException(f"Error generating itinerary", e)
            