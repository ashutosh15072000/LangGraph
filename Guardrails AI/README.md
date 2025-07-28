## Introduction

Guardrails is a framework that validates and structures data from language models. These validations range simple checks like regex matching to more complex checks like competitor analysis. Guardrails can be used with any language model.

### Installation

**Download Guardrails (required)**

First, install Guardrails for your desired language:

```
pip install guardrails-ai
```

### Generate an API Key (required)

Next, get a free API key from Guardrails Hub. Copy and keep track of this API key because you'll use it in the next step to configure the CLI.

### Configure the Guardrails CLI (required)

Configure the Guardrails CLI with the command:

```
guardrails configure
```
The configuration process will ask you three questions:

- Whether you want to enable metrics reporting.
- Whether you want to use our hosted remote inference endpoints for validators that utilize large ML models.
- To enter the API key you generated in the previous step. This is required in order to install validators in the next s

### Install a Validator from the Guardrails Hub

```
guardrails hub install hub://guardrails/detect_pii
```