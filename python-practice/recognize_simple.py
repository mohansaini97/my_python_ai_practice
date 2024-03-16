# Importing necessary modules
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Setting up Azure Text Analytics client
def setup_text_analytics_client(endpoint, key):
    return TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Analyzing reviews to recognize entities
def analyze_reviews(client, reviews):
    recognized_entities = []
    for review in reviews:
        result = client.recognize_entities(review)
        for entity in result.entities:
            if entity.category == 'Organization':
                recognized_entities.append((entity.text, review))
    return recognized_entities

# Printing recognized organizations and their associated reviews
def print_organization_reviews(organization_to_reviews):
    for organization, reviews in organization_to_reviews.items():
        print(f"\n\nOrganization '{organization}' has left us the following review(s):")
        for review in reviews:
            print(review)

# Main function
def main():
    # Retrieving Azure Text Analytics service endpoint and key from environment variables
    endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
    key = os.environ["AZURE_LANGUAGE_KEY"]

    # Initializing Text Analytics client
    text_analytics_client = setup_text_analytics_client(endpoint, key)

    # Reviews to be analyzed
    reviews = [
        "I work for Foo Company, and we hired Contoso for our annual founding ceremony. The food was amazing and we all can't say enough good words about the quality and the level of service.",
        "We at the Foo Company re-hired Contoso after all of our past successes with the company. Though the food was still great, I feel there has been a quality drop since their last time catering for us. Is anyone else running into the same problem?",
        "Bar Company is over the moon about the service we received from Contoso, the best sliders ever!!!!"
    ]

    # Analyzing reviews to recognize entities
    recognized_entities = analyze_reviews(text_analytics_client, reviews)

    # Grouping reviews by organization
    organization_to_reviews = {}
    for entity, review in recognized_entities:
        if entity not in organization_to_reviews:
            organization_to_reviews[entity] = []
        organization_to_reviews[entity].append(review)

    # Printing recognized organizations and their associated reviews
    print_organization_reviews(organization_to_reviews)

# Running the main function
if __name__ == "__main__":
    main()
