import os
import typing
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

endpoint = "https://language9784.cognitiveservices.azure.com/"
key = "14038f3af04d454f92cd061867b540ba"

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
reviews = [
    """I work for Foo Company, and we hired Contoso for our annual founding ceremony. The food
    was amazing and we all can't say enough good words about the quality and the level of service.""",
    """We at the Foo Company re-hired Contoso after all of our past successes with the company.
    Though the food was still great, I feel there has been a quality drop since their last time
    catering for us. Is anyone else running into the same problem?""",
    """Bar Company is over the moon about the service we received from Contoso, the best sliders ever!!!!"""
]

# [RecognizeEntitiesResult(id=0, entities=[CategorizedEntity(text=Foo Company, category=Organization, subcategory=None, length=11, offset=11, confidence_score=0.98), CategorizedEntity(text=Contoso, category=Person, subcategory=None, length=7, offset=37, confidence_score=0.84), CategorizedEntity(text=annual, category=DateTime, subcategory=Set, length=6, offset=53, confidence_score=1.0), CategorizedEntity(text=founding ceremony, category=Event, subcategory=None, length=17, offset=60, confidence_score=0.88), CategorizedEntity(text=food, category=Product, subcategory=None, length=4, offset=83, confidence_score=0.74)], warnings=[], statistics=None, is_error=False, kind=EntityRecognition),


result = text_analytics_client.recognize_entities(reviews)
result = [review for review in result if not review.is_error]
organization_to_reviews: typing.Dict[str, typing.List[str]] = {}

for idx, review in enumerate(result):
    for entity in review.entities:
        print(f"Entity '{entity.text}' has category '{entity.category}'")
        if entity.category == 'Organization':
            organization_to_reviews.setdefault(entity.text, [])
            organization_to_reviews[entity.text].append(reviews[idx])

for organization, reviews in organization_to_reviews.items():
    print(
        "\n\nOrganization '{}' has left us the following review(s): {}".format(  organization, "\n\n".join(reviews))
    )