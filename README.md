# JCKKRR

CS180 Project

Weekly Progress Report: https://docs.google.com/presentation/d/1QRMTpv0JVfkXvvcTMsk2Lu5KDSAgMap01XvhOzh1B2Y/edit?usp=sharing


# Instructions to Run

# Frontend

1. In terminal, run : `cd frontend`

2. In terminal type : `npm start`

# Backend

1. In a new terminal, run: `cd backend`
2. Run the automation script:
   - For Windows: In terminal: `./for_windows_setup_and_run.bat`
   - For Mac: In terminal: `chmod +x for_mac_setup_and_run.sh && ./for_mac_setup_and_run.sh`
  
# Testing

PyTest Testing Suite File Location

- `backend/test_B.py`

Pytest Framework
   1. Open the file "firebase.py" located with this relative path: `backend/FirebaseAccess/firebase.py`
   2. Ensure that line 24 is commented out and line 25 is not commented out.
      -  This should be your credentials `cred = credentials.Certificate('jokerker-d9272-firebase-adminsdk-sbyd5-fda51193ba.json')`
   4. In a new terminal, run: `cd backend`
   5. Run the automation script:
      - `pytest -v --cov=GameModule --cov=UserModule --cov-report html test_B.py`
         - The output in the terminal should include all of our test case names along with their outcome with the combined total of successful/failing tests.
         - A perfect testing run should consist of 40/40 successful tests.
           
Code Coverage Report
   1. After running the Pytest Framework, please locate the index.hmtl file with this relative path: `backend/htmlcov/index.html`
   2. Simply open it in a browser and you should be brought to the hmtl file which is able to be manipulated.
   3. If you would like to see which lines we specifically missed, simply click on the file and it should show a view with code that was reached/missing. 

