
# Django
from django.conf import settings

# Utlis
import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion


def ask_foo(kernel):

    # Prepare OpenAI service using credentials stored in the `.env` file
    service_id="chat-gpt"
    kernel.add_service(
        OpenAIChatCompletion(
            service_id=service_id,
            ai_model_id="gpt-3.5-turbo",
            api_key=settings.OPENAI_API_KEY,
        )
    )

    # Define the request settings
    req_settings = kernel.get_service(service_id).get_prompt_execution_settings_class()(service_id=service_id)
    req_settings.max_tokens = 2000
    req_settings.temperature = 0.7
    req_settings.top_p = 0.8

    prompt = """
    1) A robot may not injure a human being or, through inaction,
    allow a human being to come to harm.

    2) A robot must obey orders given it by human beings except where
    such orders would conflict with the First Law.

    3) A robot must protect its own existence as long as such protection
    does not conflict with the First or Second Law.

    Give me the TLDR in exactly 5 words."""

    prompt_template_config = sk.PromptTemplateConfig(
        template=prompt,
        name="tldr",
        template_format="semantic-kernel",
        execution_settings=req_settings,
    )

    function = kernel.create_function_from_prompt(
        function_name="tldr_function",
        plugin_name="tldr_plugin",
        prompt_template_config=prompt_template_config,
    )

    function_2 = kernel.create_function_from_prompt(
        function_name="tldr_function",
        plugin_name="tldr_plugin",
        prompt="{{$input}}\n\nOne line TLDR with the fewest words.",
        prompt_template_settings=req_settings,
    )

    return function, function_2

async def main():
    kernel = sk.Kernel()
    function, function_2 = ask_foo(kernel)
    result = await kernel.invoke(function)
    print(result)
    print(await kernel.invoke(function_2, input="""
    1st Law of Thermodynamics - Energy cannot be created or destroyed.
    2nd Law of Thermodynamics - For a spontaneous process, the entropy of the universe increases.
    3rd Law of Thermodynamics - A perfect crystal at zero Kelvin has zero entropy."""))

    # function_2 the laws of motion
    print(await kernel.invoke(function_2, input="""
    1. An object at rest remains at rest, and an object in motion remains in motion at constant speed and in a straight line unless acted on by an unbalanced force.
    2. The acceleration of an object depends on the mass of the object and the amount of force applied.
    3. Whenever one object exerts a force on another object, the second object exerts an equal and opposite on the first."""))

    # function_2 the law of universal gravitation
    print(await kernel.invoke(function_2, input="""
    Every point mass attracts every single other point mass by a force acting along the line intersecting both points.
    The force is proportional to the product of the two masses and inversely proportional to the square of the distance between them."""))

if __name__ == "__main__":
    asyncio.run(main())
