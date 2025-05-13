# Python Baseline Practices
Python baseline practice: Accu Weather

---

## Setup Python Virtual Environment

To isolate dependencies and ensure a clean environment, it's recommended to use a Python virtual environment.

### On Unix or macOS:
Run below command to setup you virtual env
```bash
python3 -m venv env
source env/bin/activate
```

### On Windows 
Using cmd:
```
python -m venv env
.\env\Scripts\activate
```

Using PowerShell:
```
python -m venv env
.\env\Scripts\Activate.ps1
```

### Installing Dependencies
Install the project dependencies listed in requirements.txt. If you don't have this file, please ensure to add your dependencies accordingly.
```
pip install -r requirements.txt
```

### Running Tests with pytest
Make sure your virtual environment is activated, then run:

```
pytest
```
<small>Note: This would run all existing tests in the project</small>

Alternatively, you can:
* Run a specific test file by running: `pytest path/to/test_file.py`
* Run tests with verbose output with: `pytest -v`

To see detailed test reports or debug, explore pytest options in `pytest --help.`

### License Information
This Software is distributed through [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.html)
