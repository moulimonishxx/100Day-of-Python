
# Password Generator App

## Overview

The **Password Generator App** is a simple yet powerful Python application that allows users to generate strong, secure passwords. The app provides a user-friendly graphical interface built using the `Tkinter` library, which allows users to customize the generated password based on their requirements. The app utilizes Python's built-in `secrets` module for generating cryptographically secure random passwords.

This app is ideal for generating strong passwords for various online accounts and applications where security is important. Users can control the password length, choose which types of characters to include (e.g., uppercase letters, lowercase letters, digits, symbols), and even input custom characters.

## Features

- **Customizable Password Length**: Users can choose the length of the generated password from 8 to 32 characters.
- **Character Selection**: Choose to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Symbols (e.g., !, @, #, $, etc.)
- **Custom Character Input**: Add custom characters to the password by specifying them in the input box.
- **Generate Button**: Securely generates a password based on the user’s selection and inputs.
- **Copy to Clipboard**: Copy the generated password to the system clipboard with a single click.
- **Clear Button**: Reset the inputs and generated password to the default state.
- **Responsive Design**: The UI adapts to different screen sizes for ease of use.

## Screenshots

### Sapmles

![Image 1](https://i.ibb.co/bzLDsrf/Screenshot-2024-12-27-120232.png)
![Image 2](https://i.ibb.co/xqgZNFg/Screenshot-2024-12-27-120247.png)
![Image 3](https://i.ibb.co/JxRQmgB/Screenshot-2024-12-27-120332.png)
![Image 4](https://i.ibb.co/hRHw5gL/Screenshot-2024-12-27-120353.png)



### Copy Option
![Generated Password](https://i.ibb.co/P4SZPgP/Screenshot-2024-12-27-120404.png)

## Requirements

- Python 3.x or higher
- Tkinter (for GUI development)
- `pyperclip` (for clipboard functionality)

### Install Dependencies

You can install the required libraries using `pip`. In your terminal or command prompt, run the following command:

```bash
pip install pyperclip
```

**Note:** Tkinter should be included by default with most Python installations. If it is not installed, you can install it separately based on your operating system.

### Install Python

If you don't have Python installed on your system, you can download it from the official Python website:

[Download Python](https://www.python.org/downloads/)
## Installation

1. Clone or download this repository:

    ```bash
    git clone https://github.com/moulimonishxx/100Day-of-Python/tree/main/PasswordGenerator
    ```

2. Navigate to the project directory:

    ```bash
    cd PasswordGenerator
    ```

3. Run the application:

    ```bash
    python PasswordGenerator
    ```

## Usage

1. **Run the Application**:
   To start the app, navigate to the folder containing `main.py` and run the following command:

   ```bash
   python main.py
   ```

2. **Customize the Password**:
   - Select the **Password Length** (default: 12 characters).
   - Check or uncheck the options for uppercase, lowercase, digits, and symbols.
   - Optionally, add any **Custom Characters** you want to include in the password.

3. **Generate Password**:
   Click the **Generate** button to create a password based on the options you've selected.

4. **Copy Password**:
   After generating the password, click the **Copy** button to copy it to your clipboard.

5. **Clear Fields**:
   Click the **Clear** button to reset all fields, including the generated password.

## Sample Outputs

### Example 1:
- **Password Length**: 12 characters
- **Character Types**: Uppercase, Lowercase, Digits, Symbols
- **Custom Characters**: `!@#`
- **Generated Password**: `9tH@p8zD!XzA`

### Example 2:
- **Password Length**: 16 characters
- **Character Types**: Uppercase, Lowercase
- **Custom Characters**: `xyz`
- **Generated Password**: `CjDxyzAyTLfsRqZ1L`

### Example 3:
- **Password Length**: 8 characters
- **Character Types**: Digits, Symbols
- **Custom Characters**: `&*`
- **Generated Password**: `8b%9*D1x`

### Example 4 (with Custom Characters):
- **Password Length**: 10 characters
- **Character Types**: Uppercase, Lowercase
- **Custom Characters**: `ABC`
- **Generated Password**: `f4AsC@z9CB`

## Technical Details

### Key Libraries Used:

- **Tkinter**: For building the graphical user interface (GUI).
- **pyperclip**: A module used to copy the generated password to the clipboard.
- **secrets**: Python's `secrets` module is used to generate cryptographically secure passwords.

### Core Functionality:

1. **Password Generation**: Based on the user input, the password is randomly generated with the specified length and character options using the `secrets` library. The generated password is displayed in a text box.
   
2. **Clipboard Copying**: The password can be copied to the clipboard using the `pyperclip` library. This allows users to easily paste the password into any application that requires it.

3. **Clear Functionality**: Clicking the "Clear" button resets the app, including the selected options and generated password.

## Author

- **Author**: Moulimonish S.
- **Contact**: You can reach out to me on [LinkedIn](https://www.linkedin.com/in/moulimonishs).
  
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contribution

Contributions are welcome! If you'd like to improve this project or add new features, feel free to open an issue or submit a pull request.

---

Feel free to modify and use this project as per your needs. If you find any issues or have any questions, don't hesitate to reach out.
