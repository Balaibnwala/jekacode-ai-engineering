# Step 2 — Install Python

Python is the language we use to talk to computers and to AI.

## Mac

1. Open **Terminal**.
2. Paste this and press Enter:

```bash
python3 --version
```

3. You want a number that is **3.11 or higher**, for example `Python 3.11.9`.
4. If the command fails, install Python from [https://www.python.org/downloads](https://www.python.org/downloads) and tick **Add Python to PATH** if you see that box.

## Windows

1. Open **PowerShell**.
2. Run:

```powershell
python --version
```

3. You want **3.11 or higher**.
4. If Windows opens the Microsoft Store instead, install Python 3.12 from [python.org](https://www.python.org/downloads) and tick **Add python.exe to PATH**.

## Create a safe classroom folder for packages

In VS Code, open the Terminal (**Terminal → New Terminal**) and run these commands **one at a time**:

**Mac:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
python -m ipykernel install --user --name jekacode --display-name "Python (Jekacode)"
```

**Windows:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
python -m ipykernel install --user --name jekacode --display-name "Python (Jekacode)"
```

If Windows says scripts are disabled, run this once, then try Activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

When it works, your terminal line will start with `(.venv)`.

## How to pick the right kernel in a notebook

1. Open any `.ipynb` file.
2. Top right, click **Select Kernel**.
3. Choose **Python (Jekacode)** or the `.venv` Python.

Next: [03_github.md](03_github.md)
