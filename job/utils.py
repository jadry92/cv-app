""" Thi module contains utility functions for the app job """

# GPT-3 API
from openai import OpenAI

# Django
from django.conf import settings
from django.contrib import messages

# Models
from job.models import JobDetails, Job

# Utils
import json


def request_analysis(raw_description):
    """This function sends a request to the GPT-3 API to analyze the raw description
        Example of the response:

    {
        "key_points": [
        ],
        "role": {
            "title": "Software Developer",
            "responsibilities": [
            ],
            "qualifications": [
            ],
            "location": "Australia",
            "work_options": "3 days in office, 2 days from home",
            "requirement": "Must have the right to work in Australia",
        },
        "summary": "",
    }

    """

    # Set the API key
    client = OpenAI(api_key=settings.CHAT_GPT_API_KEY)

    # Set the prompt
    prompt = f"Analyze the following job description and provide key points, role and a summary: \n\n{raw_description}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": prompt},
        ],
    )

    raw_analysis = response.choices[0].message.content
    if not raw_analysis:
        raise ValueError("the response was empty")

    analysis = json.loads(raw_analysis)

    return (analysis, response.usage)
