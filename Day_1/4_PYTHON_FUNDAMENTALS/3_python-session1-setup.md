# Personal Notes: Python Series -- Session 1 Setup (VS Code + Virtual Environment)

------------------------------------------------------------------------

## 1. Environment Overview

For my Python journey, I'll be using:

-   **VS Code** as my main IDE\
    → It supports both `.py` scripts and `.ipynb` notebooks, plus great
    extensions and debugging tools.

-   **Python 3.12**\
    → The course covers features from Python 3.10 to 3.12, so using the
    latest version makes sense.

------------------------------------------------------------------------

## 2. Why I Need a Virtual Environment

Creating a virtual environment keeps things clean and isolated.

### ✔️ Benefits:

-   Prevents version conflicts between different projects\
-   Keeps dependencies stable even when global packages update\
-   Makes the project environment reproducible and easier to share

This is especially important for Data Science, where libraries update
frequently.

------------------------------------------------------------------------

## 3. Setting Up My Environment (Step-by-Step)

### 🟩 Step A: Create the Environment

Open CMD/Terminal inside VS Code and run:

``` bash
conda create -p venv python==3.12
```

-   `-p venv` → creates the environment inside a folder named `venv`
-   Python version is explicitly set to **3.12**

Confirm with **y** when asked.

------------------------------------------------------------------------
 
### 🟩 Step B: Activate the Environment

``` bash
conda activate venv/
```

Once activated, the terminal typically shows `(venv)` at the beginning.

------------------------------------------------------------------------

## 4. Running Python Code

------------------------------------------------------------------------

### Scenario A: Running a `.py` Script

1.  Create a new file → `app.py`
2.  Write:

``` python
print(1 + 1)
```

3.  Run it:

``` bash
python app.py
```

Expected Output → `2`

------------------------------------------------------------------------

### Scenario B: Running a `.ipynb` Notebook in VS Code

1.  Create a file → `test.ipynb`
2.  Click **Select Kernel**\
    Choose:
    -   Python Environments\
    -   The environment I created (`venv` / Python 3.12)
3.  If I get this message:

```{=html}
<!-- -->
```
    Running cells requires ipykernel

I simply install it:

``` bash
pip install ipykernel
```

4.  Now run any cell with **Shift + Enter**

Example:

``` python
print("Hello World")
```

------------------------------------------------------------------------

## 5. Using `requirements.txt`

To keep dependencies organized:

-   Add every installed package (e.g., `ipykernel`, `pandas`, `numpy`)
    to `requirements.txt`.
-   Later, I can install all packages at once with:

``` bash
pip install -r requirements.txt
```

This is great for sharing projects or rebuilding environments.

------------------------------------------------------------------------

## 6. Summary of Key Commands

  Action                  Command
  ----------------------- -------------------------------------
  **Create Env**          `conda create -p venv python==3.12`
  **Activate Env**        `conda activate venv/`
  **Run Python File**     `python filename.py`
  **Install Package**     `pip install package_name`
  **Run Notebook Cell**   Shift + Enter

------------------------------------------------------------------------

These notes help me remember the full setup process smoothly whenever I
start a new project.
