# talesGPT

[![Python 3.11](https://github.com/andreaxricci/talesGPT/actions/workflows/main.yml/badge.svg)](https://github.com/andreaxricci/talesGPT/actions/workflows/main.yml)

This simple app shows how to combine the Azure Speech service and Langchain, in order to generate and narrate stories, based on a given input.

Step 1: Using the Azure Speech service, the user voice is converted from Speech-to-text, and used as input for the next step

Step 2: The user input is passed via Langchain to a LLM, which generates the story

Step 3: The story is narrated, using the synthesiser service from Azure Speech

<img width="1302" alt="Screenshot 2023-06-23 at 09 46 38" src="https://github.com/andreaxricci/talesGPT/assets/62494809/6cb323fb-c553-4de8-8cdb-f0d1d2b27ebc">

<img width="1297" alt="Screenshot 2023-06-23 at 09 48 37" src="https://github.com/andreaxricci/talesGPT/assets/62494809/1364c3c5-0cc4-483e-9775-05b70fc2b04a">

<img width="1305" alt="Screenshot 2023-06-23 at 09 49 51" src="https://github.com/andreaxricci/talesGPT/assets/62494809/63310faa-7ed0-458a-9d3b-a5b5acbc1996">



