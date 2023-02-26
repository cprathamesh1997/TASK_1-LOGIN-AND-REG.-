## TASK_1-LOGIN-AND-REGISTRATION SYSTEM
## Registration and Login system using Python, file handling.
The program is a registration and login system implemented using Python and file handling. It has three stages:

Stage 1: Registration
When the user chooses to register, they must enter a valid email or username that should have "@" and followed by "." (e.g., sherlock@gmail.com), and it should not start with special characters or numbers (e.g., 123#@gmail.com). The password must be between 5 to 16 characters and contain at least one special character, one digit, one uppercase and one lowercase character.

Stage 2: Once the username and password are validated, the program stores that data in a file named "Access_file.csv".

Stage 3: Login
When the user chooses to login, the program checks whether their credentials exist in the "Access_file.csv" file or not based on the user input. If the credentials don't exist, the program asks the user to either register or retrieve their original password based on their username. If the username matches with the data that exists in the file, the program retrieves the original password. If nothing matches in the file, the program asks the user to register since they don't have an account.

The program uses regular expressions to validate the email and password inputs and uses the csv module to read and write data to the file.
