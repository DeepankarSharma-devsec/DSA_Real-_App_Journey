# Personal Notes: Setting Up My Python Development Environment (Anaconda + VS Code)

------------------------------------------------------------------------

## 1. Overview

For my Data Science and AI workflow, I need two core tools:

-   **Anaconda** → handles environments, packages, and version
    management\
-   **VS Code** → my main coding editor (for both `.py` and `.ipynb`
    files)

Having both properly installed makes the whole setup smooth and avoids
dependency issues later.

------------------------------------------------------------------------

## 2. Installing Anaconda

### ✔️ Why I'm Using Anaconda

-   Manages isolated environments\
-   Avoids version conflicts\
-   Makes installing scientific libraries easier\
-   Works perfectly with Jupyter, VS Code, and PySpark setups

------------------------------------------------------------------------

### ✔️ Installation Steps (What I Did)

1.  **Download from:**\
    `anaconda.com` → Free Download → Enter email → Choose OS
    (Windows/Mac/Linux)

2.  **Run the Installer**

    -   Open the `.exe` file\
    -   Click **Next** → **I Agree**\
    -   Choose **Just Me**

3.  **Choose Installation Location**

    -   Default goes to: `C:\\Users\\Name\\anaconda3`\
    -   I can choose another drive (like `E:`) if I want to save C drive
        space.

4.  **Important Step (VERY IMPORTANT)**\
    There is an option:

        Add Anaconda3 to my PATH environment variable

    ✔️ **I checked this**, even though it says "Not Recommended".

    **Reason:**\
    I want to run `conda`, `python`, and `pip` directly from Command
    Prompt.

5.  **Click Install** and wait.

------------------------------------------------------------------------

### ✔️ Verifying Installation

I searched for **Anaconda Navigator** in the Start Menu → opened it →
dashboard loaded fine.\
This confirmed the installation was successful.

------------------------------------------------------------------------

## 3. Installing VS Code

1.  Download VS Code from the official site.\
2.  Run the installer → Click **Next** → **Finish**.\
3.  Done. Quick and clean install.

------------------------------------------------------------------------

## 4. Launching VS Code From Command Line (My Preferred Workflow)

### ✔️ Steps I Follow

1.  Create a project folder:

        Data Analyst Bootcamp/Python

2.  Open Command Prompt / Terminal.

3.  Navigate into the folder:

    ``` bash
    cd D:\AI\DSA_Real _App_Journey\Day_1\4_PYTHON_FUNDAMENTALS
    ```

4.  Launch VS Code inside the folder:

    ``` bash
    code .
    ```

This opens VS Code with the current directory as a workspace --- super
convenient.

------------------------------------------------------------------------

## 5. Troubleshooting Notes (from Experience)

### ✔️ If `conda` or `pip` don't work:

-   PATH variables were probably not added correctly.
-   Anaconda's `/Scripts` and `/Library/bin` must be in the environment
    variables.

### ✔️ If VS Code causes issues:

-   Install/Update the Python extension inside VS Code.
-   Use **Google Colab** temporarily to keep learning without
    interruptions.

------------------------------------------------------------------------

These notes help me quickly set up or reset my Python environment
anytime I need it.
