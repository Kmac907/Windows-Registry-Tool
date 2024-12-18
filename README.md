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

