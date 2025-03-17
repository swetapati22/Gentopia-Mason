# Gentopia-Mason

**Gentopia-Mason is a framework designed for creating and managing LLM agents with different capabilities.** I am running this project and adding an additional functionality to it, specifically enhancing it with a **Currency Conversion Agent** that integrates real-time exchange rate retrieval using the Fixer.io API.

**IMPORTANT NOTICE: This code repository was adapted from [Gentopia.AI](https://github.com/Gentopia-AI) to support Mason Activities.**

Author: Ziyu Yao (ziyuyao@gmu.edu)
Copyright and license should go to Gentopia.AI.

## Installation 💻
First, clone this repository:
```
git clone git@github.com:LittleYUYU/Gentopia-Mason.git
cd Gentopia-Mason
```
Next, we will create a virtual environment and install the library:
```
conda create --name gentenv python=3.10
conda activate gentenv
pip install -r requirements.txt
```

Most of the agent construction and execution activities will happen within `GentPool`. For the `gentopia` library to be used within `GentPool`, set up the global environment:
```
export PYTHONPATH="$PWD/Gentopia:$PYTHONPATH"
```
In addition, since we will be using OpenAI's API, we also need to create a `.env` file under `GentPool` and put the API Key inside. The key will be registered as environmental variables at run time.
```
cd GentPool
touch .env
echo "OPENAI_API_KEY=<your_openai_api_key>" >> .env
```
Now you are all set! Let's create your first Gentopia Agent.

## Quick Start: Clone a Vanilla LLM Agent
GentPool has provided multiple template LLM agents. To get started, we will clone the "vanilla agent" from `GentPool/gentpool/pool/vanilla_template` with the following command:
```
./clone_agent vanilla_template <your_agent_name> 
```
This command will initiate an agent template under `./GentPool/gentpool/pool/<your_agent_name>`. The agent configuration can be found in `./GentPool/gentpool/pool/<your_agent_name>/agent.yaml` (note the agent type `vanilla`). The vanilla prompt it uses can be found in the source code of `Gentopia`; see `./Gentopia/gentopia/prompt/vanilla.py`.

You can now run your agent via:
```
python assemble.py <your_agent_name>
```
This vanilla agent simply sends the received user query to the backend LLM and returns its output. Therefore, for many complicated tasks, such as those requiring accessing the latest materials, it will fail. 

## Implement a Scholar LLM Agent with Tool Augmentation
In the second trial, we will create a Scholar agent which is augmented with multiple functions to access Google Scholar in real time.

This is based on the `scholar` agent we have created in the pool. As before, in this demo we simply clone it:
```
./clone_agent scholar <your_agent_name> 
```
Like before, this command created an agent under `./GentPool/gentpool/pool/<your_agent_name>`. Note from its configuration that scholar is an `openai`-type agent. As stated in its [Gentopia's implementation](./Gentopia/gentopia/agent/openai), this type of agent allows for function calling:
> OpenAIFunctionChatAgent class inherited from BaseAgent. Implementing OpenAI function call api as agent.

The available functions to the scholar agent have been listed in its configuration file `./GentPool/gentpool/pool/<your_agent_name>/agent.yaml`, and the implementation of these tools can be found in Gentopia's source code (mostly coming from the [google_scholar.py](./Gentopia/gentopia/tools/google_scholar.py) file, in this example).

Now, you are all set to query this scholar agent for the latest papers by certain authors, the summary of a certain paper, paper citations, etc.

## Remove an Agent
Sometimes an agent can upset you. To wipe it out completely,
```
./delete_agent <your_agent_name> 
```

## **New Feature: Currency Conversion Agent**
As an extension of this project, I have developed a **Currency Conversion Agent** that provides real-time currency conversion using the **Fixer.io API**. This agent allows users to convert from any currency to any other currency dynamically, leveraging the latest exchange rates.

### **How It Works**
- The agent retrieves real-time currency conversion values from **Fixer.io API**.
- The user query triggers an API call to fetch the latest exchange rates.
- The system ensures that conversions are always **up-to-date**.

### **Setup for Currency Conversion Agent**
This agent is based on the existing `scholar` agent template. To integrate it:
```
./clone_agent scholar currency_conversion_agent
```
Once cloned, update the agent configuration in `agent.yaml` as follows:

#### **Modify the following fields in `agent.yaml`:**
- **Set the model**:
  ```yaml
  model_name: gpt-3.5-turbo
  ```
- **Add the Plugin**:
  ```yaml
  Plugins:
    - name: currency_conversion
  ```
- **Define the target task**:
  ```yaml
  target_tasks:
    - currency conversion
  ```

### **Running the Currency Conversion Agent**
To execute the agent, run:
```
python assemble.py currency_conversion_agent
```

With this setup, the agent efficiently provides real-time currency exchange rates and conversions on demand.

---

## **New Feature: PDF Reader Agent**
As an enhancement to **Gentopia-Mason**, I have developed a **PDF Reader Agent** that extracts and reads text from PDF documents available online.

### **How It Works**
- Accepts a **PDF URL** as input.
- Downloads and extracts **text content** from the PDF file.
- Returns a **readable output** for analysis.

### **Setup for PDF Reader Agent**
Clone the `scholar` agent template:
```bash
./clone_agent scholar pdf_reader_agent
```
Modify `agent.yaml` to include the new tool:
```yaml
Plugins:
  - name: pdf_reader
```
```yaml
target_tasks:
  - pdf document reading
```

### **Running the PDF Reader Agent**
Execute:
```bash
python assemble.py pdf_reader_agent
```
With this setup, the **PDF Reader Agent** can **fetch, process, and extract text from online PDFs**, making document analysis easier.

---

This project extends Gentopia with:
**Currency Conversion Agent**: AI-driven **real-time currency conversion** using **Fixer.io API**.  
**PDF Reader Agent**: Reads and extracts **text from online PDFs** for easier document analysis.

This project extends **Gentopia** with **practical AI applications**, making it **smarter, more interactive, and highly resourceful**.
