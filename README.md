# Software-Engineer-
Develop a software - Doctor call App

Inside this program, there are 3 characters which are the user, doctor, and admin. Besides also has main pages that show different pages when the condition is met, and transfer the data such as username, clinic_name, and doctor_name between pages and pages. Thus, also with a firebase_config which contains the Firebase real-time database that supports the fetching and inserting data.

For the user, have those pages
1. Login page
   - Able to validate incorrect username and password
2. Register page
   - Able to validate with database on can't have the same username, email contact number, and both passwords must be same
3. Forgot password page
   - Before the user resets the password, will need to validate whether the username and email exist or not else, will show data not found
4. Reset password page
   - After the user enters the correct username, an email will show this reset password page, and both the passwords provided must be the same
5. Appointment page
   - This page will show all the appointments that have been made by that user with the appointment details
6. Booking page
  - Able to make an appointment with a doctor in that clinic
  - Able to show the doctor's busy date
  - Able to do validation on can't select pass time and date
7. Home page
   - Able to show the user's height and weight and calculate BMI
   - Able to show recent appointments with details
   - Able to show that appointment prescription
   - Able to show suggestion doctor (random 2 doctors)
8. Search clinic page
   - Able to show all the clinic
9. User settings page
   - Able to update the information by each
10. User showing prescriptions page
   - Able to show that appointment prescription
11. User sidebar page
  - Able to show the user sidebar and call in every user pages
12. The user views the clinic page
    - Able to view the details of the clinic
13. The user views the doctor's page
  - Able to list down all the existing doctors in that clinic

For the doctors, have those pages
1. The doctor generates a prescription page
   - Able to all the related user's appointment details after the user have entered the username, and given out some medical instructions
2. Doctor home page
  - Able to show current or upcoming appointments with which user describe their problem
3. Doctor login page
  - Able to validate incorrect username and password
4. Doctor view patient record page
  - Able to view previous prescriptions of that user and able to make modify the medical and instructions
5. Doctor sidebar page
  - Able to show the doctor sidebar and call in every doctor's page

For the admin, have those pages
1. Admin add doctor page
  - Able to add a new doctor
2. Admin assign doctor page
  - Able to assign a doctor to that user on a specific date and time
3. Admin home page
  - Able to view all the pending requests for the appointment, and approve or reject the appointment by changing the status from false(pending) to either true(accepted or false(rejected)
4. Admin login page
  - Able to validate incorrect username and password
5. Admin shows clinic page
  - Able to list down all the existing clinic
6. Admin show doctor on the clinic page
  - Able to show that specific doctor in a specific clinic with some details
7. Admin views doctors in the clinic
  - Able to list down all the existing doctors inside that clinic
8. Admin sidebar page
  - Able to show the admin sidebar and call in every admin page






