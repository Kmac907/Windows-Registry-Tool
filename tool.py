import winreg


def update_registry_paths(old_path, new_path):
    updated_keys = []

    def search_and_replace_key(hive, key):
        try:
            with winreg.OpenKey(
                hive, key, 0, winreg.KEY_READ | winreg.KEY_WRITE
            ) as reg_key:
                i = 0
                while True:
                    try:
                        value_name, value_data, value_type = winreg.EnumValue(
                            reg_key, i
                        )
                        if isinstance(value_data, str) and old_path in value_data:
                            new_value = value_data.replace(old_path, new_path)
                            winreg.SetValueEx(
                                reg_key, value_name, 0, value_type, new_value
                            )
                            updated_keys.append((hive, key, value_name))
                        i += 1
                    except OSError:
                        break

                j = 0
                while True:
                    try:
                        subkey_name = winreg.EnumKey(reg_key, j)
                        subkey_path = f"{key}\\{subkey_name}" if key else subkey_name
                        search_and_replace_key(hive, subkey_path)
                        j += 1
                    except OSError:
                        break
        except FileNotFoundError:
            pass

    # Hives to search
    hives = [
        winreg.HKEY_LOCAL_MACHINE,
        winreg.HKEY_CURRENT_USER,
        winreg.HKEY_CLASSES_ROOT,
        winreg.HKEY_USERS,
        winreg.HKEY_CURRENT_CONFIG,
    ]

    for hive in hives:
        search_and_replace_key(hive, "")

    return updated_keys


if __name__ == "__main__":
    old_path = input("Enter the old file path: ").strip()
    new_path = input("Enter the new file path: ").strip()

    print("Updating registry paths... This may take a while.")
    updated_keys = update_registry_paths(old_path, new_path)

    if updated_keys:
        print("Updated registry locations:")
        for hive, key, value_name in updated_keys:
            print(f"Hive: {hive}, Key: {key}, Value: {value_name}")
    else:
        print("No registry entries were updated.")
