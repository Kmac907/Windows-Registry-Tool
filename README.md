# Update Windows Registry Paths

This Python script updates all occurrences of a specified old file path in the Windows registry with a new file path. It recursively scans all registry hives and logs the registry locations that were updated.

## Features
- Scans all major Windows registry hives:
  - `HKEY_LOCAL_MACHINE`
  - `HKEY_CURRENT_USER`
  - `HKEY_CLASSES_ROOT`
  - `HKEY_USERS`
  - `HKEY_CURRENT_CONFIG`
- Replaces the old file path with the new file path wherever found.
- Logs all registry keys and values that were updated.

## Prerequisites
- **Python 3.x**
- **Admin Privileges:** The script requires administrative privileges to modify the Windows registry.

## Usage

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### Step 2: Run the Script
1. Open a terminal with administrative privileges.
2. Run the script:
   ```bash
   python update_registry_paths.py
   ```
3. Enter the old file path and the new file path when prompted.

### Example
If you want to replace `C:\old\path\to\test` with `C:\new\path\to\test`, you would run the script as follows:

```plaintext
Enter the old file path: C:\old\path\to\test
Enter the new file path: C:\new\path\to\test
```

The script will search the registry and replace all occurrences of the old path with the new path.

## Testing
To safely test the script:
1. Create a dummy registry key and value:
   - Key: `HKEY_CURRENT_USER\Software\TestKey`
   - Value: `C:\old\path\to\test`
2. Run the script with the old path `C:\old\path\to\test` and new path `C:\new\path\to\test`.
3. Verify that the registry value is updated.

You can also automate the setup of the test key using the provided test setup script:

```python
import winreg

def create_test_registry_key():
    key_path = r"Software\\TestKey"
    try:
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            winreg.SetValueEx(key, "TestValue", 0, winreg.REG_SZ, "C:\\old\\path\\to\\test")
        print("Test registry key created.")
    except Exception as e:
        print(f"Error creating test key: {e}")

if __name__ == "__main__":
    create_test_registry_key()
```

## Script Explanation

### 1. Main Function: `update_registry_paths`
- **Purpose:** Takes two inputs:
  - `old_path`: The file path to search for in the registry.
  - `new_path`: The file path to replace the `old_path`.
- **Returns:** A list of registry keys and values that were updated.

### 2. Nested Function: `search_and_replace_key`
This recursive function is responsible for:
1. **Opening a Registry Key:**
   - Uses `winreg.OpenKey` to access a specific registry key.
   - Opens the key with read and write permissions (`KEY_READ | KEY_WRITE`).

2. **Scanning Values in the Key:**
   - Uses `winreg.EnumValue` in a loop to iterate through all values in the key:
     - Retrieves the name, data, and type of each value.
     - If the data contains the `old_path` and is a string, it replaces the `old_path` with `new_path`.
     - Updates the value in the registry using `winreg.SetValueEx`.
     - Logs the updated key in the `updated_keys` list.

3. **Recursively Processing Subkeys:**
   - Uses `winreg.EnumKey` in a loop to iterate through all subkeys.
   - Constructs the full path to each subkey and recursively calls `search_and_replace_key` on it.
   - Continues until all subkeys have been processed.

4. **Error Handling:**
   - Catches `OSError` to handle the end of enumeration gracefully.
   - Handles `FileNotFoundError` to skip missing or inaccessible keys.

### 3. Registry Hives:
The script processes five main registry hives:
- `HKEY_LOCAL_MACHINE`: Configuration data for the system.
- `HKEY_CURRENT_USER`: Settings for the currently logged-in user.
- `HKEY_CLASSES_ROOT`: Information about file associations and COM objects.
- `HKEY_USERS`: Settings for all user profiles on the machine.
- `HKEY_CURRENT_CONFIG`: Settings for the current hardware profile.

### 4. Main Execution Block (`if __name__ == "__main__":`)
- **User Input:**
  - Prompts the user to enter the `old_path` and `new_path`.
  - Strips extra whitespace from the input.

- **Calling `update_registry_paths`:**
  - Prints a message indicating that the update process is starting.
  - Calls `update_registry_paths` with the input paths.

- **Output Results:**
  - If updates are made, it lists the registry locations that were modified.
  - If no changes are detected, it informs the user that no updates were made.

### 5. Core Registry Operations:
- **Enumerating Values:**
   - The script inspects all values (name-data pairs) within each registry key for matches to the `old_path`.

- **Recursive Subkey Traversal:**
   - After processing the current key's values, it moves to its subkeys, ensuring a thorough search of the entire registry tree.

### 6. Safety Features:
- **Error Handling:** Ensures the script doesn’t crash if it encounters inaccessible keys or permissions issues.
- **Non-Destructive Behavior:** Only modifies values containing the exact `old_path`.
- **Administrative Privileges:** Requires elevated permissions to make registry changes.

### 7. How to Test the Script:
The script can be tested safely by creating a dummy registry key with test data, as outlined in the README. This ensures no critical parts of the registry are affected during testing.

### Output:
- A summary of all updated registry locations is printed in the format:
  ```
  Hive: <Hive>, Key: <Registry Key>, Value: <Value Name>
  ```

This script is a robust way to bulk-update file paths in the Windows registry, especially useful during migrations or configuration changes. It ensures comprehensive coverage of the registry while handling potential errors gracefully.

## Notes
- Always **back up the registry** before running the script to avoid unintended changes.
- Use this script only in controlled environments or after thorough testing.

## Limitations
- The script only works on Windows systems.
- It modifies registry keys and values that are accessible with the user's privileges.
- Long execution times may occur for systems with large registries.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
This script is provided "as is" without warranty of any kind. Use it at your own risk.

