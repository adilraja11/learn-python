from pm import PromptManager
from pydantic import BaseModel, Field
from datetime import date

class AnalyzeEvent(BaseModel):
    is_event: bool = Field(
        description="Information of the query if contain an event"
    )
    description: str = Field(
        description="Description of event"
    )
    confidence_score: float = Field(
        description="How confident you are between 0 to 1"
    )

class EventDetail(BaseModel):
    name: str = Field(
        description="The name of the event"
    )
    description: str = Field(
        description="The description of the event"
    )
    date: str = Field(
        description="Date time of the event"
    )
    duration: str = Field(
        description="Duration of the event"
    )

def analyze_event(query):
    pm = PromptManager()
    pm.add_message(
        "user",
        query
    )

    result = pm.generate_structured(AnalyzeEvent)
    is_event = result.get('is_event')
    description = result.get('description')
    confidence_score = result.get('confidence_score')

    return is_event, description, confidence_score

def extract_event(query):
    today = date.today()
    pm = PromptManager()
    pm.add_message(
        "system",
        f"Extract event details based on user Query, as additional information today's date is {today}"
    )
    pm.add_message(
        "user",
        query
    )

    result = pm.generate_structured(EventDetail)
    print(result)

def run():
    input_query = input("Query: ")
    is_event, description, confidence_score = analyze_event(input_query)
    if is_event and confidence_score > 0.7:
        print(f"Confidence Score: {confidence_score}")
        extract_event(description)
    else:
        print("No, this is not an event.")


if __name__ == "__main__":
    run()