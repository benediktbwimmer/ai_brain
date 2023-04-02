from brain import answer_prompt, load_memory

memory = load_memory("conversation.md")
context = ""

prompt = "Please explain me again, updated with all information you can find in our conversation about CSDSLs, what is a Context Specific Domain Specific Language and how can it help understand human-ai interaction better?"

response = answer_prompt(context, prompt)
print(response)
