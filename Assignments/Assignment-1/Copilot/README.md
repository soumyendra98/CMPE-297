# Data_Mining

This assignment shows how I have used gpt-engineer to develop a application, to run unit tests, to refactor the code, etc.
Step-by-step guide:

**Setup:**

1.  Download <a href="https://code.visualstudio.com/download">VS Code</a>, if you haven't already.
2.  Inside the command prompt use below command for stable environment > `python -m pip install gpt-engineer`
3.  Then, write ``` conda create <env-name> python="version"
    conda activate <env-name> ```
5.  Then set API key:
   ` export OPENAI_API_KEY = [your api key]` for macOS
   ` set OPENAI_API_KEY = [your api key]` for windows

**How to use:**
---

1. Create an empty folder for your project in VScode.
2. Inside that folder, create a file named prompt (with no extension) and write a prompt with instruction/ operation you want to perform.
3. To call that file use cmd ` gpt-engineer <project_dir> `
   For example: gpt-engineer assignment2/data_mining

**Results:**
---

Check the generated files in projects/my-new-project/workspace

**Workflow:**
---

gpt-engineer --help lets you see all available options.


**Application Demo:**
---

A link to the video that shows an application where I have used **github copilot** and **gpt-engineer** to perform test cases and refactoring.

[![Song_Recommendation_System](https://github.com/Mansiiv/Data_Mining/assets/47898293/e1b257b0-7e48-47ae-8784-3c4e663d9382)](https://github.com/Mansiiv/Data_Mining/assets/47898293/e1b257b0-7e48-47ae-8784-3c4e663d9382)



