# talesGPT

[![Python 3.11](https://github.com/andreaxricci/talesGPT/actions/workflows/main.yml/badge.svg)](https://github.com/andreaxricci/talesGPT/actions/workflows/main.yml)

This simple app shows how to combine the Azure Speech service and Langchain, in order to generate and narrate stories, based on a given input.

Step 1: Using the Azure Speech service, the user voice is converted from Speech-to-text, and used as input for the next step

Step 2: The user input is passed via Langchain to a LLM, which generates the story

Step 3: The story is narrated, using the synthesiser service from Azure Speech
