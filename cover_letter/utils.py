""" Funtions to access chat GPT-3 API """

# GPT-3 API
from openai import OpenAI

# Django
from django.conf import settings


def request_suggestion_for_cover_letter(job_summary, cv_infor):
    """
    This function asks for asugestion when writing a cover letter base on a job description

    """
    client = OpenAI(api_key=settings.CHAT_GPT_API_KEY)
    prompt = f"Write a cover letter for a this job: \n\n {job_summary} \n\n My cv is: {cv_infor}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    usage = f"Total tokens: {response.usage.total_tokens} \n Prompt: {response.usage.prompt_tokens} \n Completion: {response.usage.completion_tokens} \n"
    return (response.choices[0].message.content, usage)
