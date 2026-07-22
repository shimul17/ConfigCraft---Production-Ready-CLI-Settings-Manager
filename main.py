import json
import os
import sys

class ConfigManager:
    def __init__(self, filename="user_config.json"):
        self.filename = filename
        self.settings = self._load_settings()

    def _load_settings(self):
        """Loads settings from the JSON file on the hard drive (Persistence)."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print(f"\n❌ [Error] Core file '{self.filename}' corrupted. Resetting memory.")
                return {}
        return {}

    def _save_settings(self):
        """Updates the JSON file whenever changes are made."""
        with open(self.filename, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def add_setting(self, key, value):
        key, value = str(key).strip().lower(), str(value).strip().lower()
        if not key or not value:
            return "⚠️ Error: Key and Value cannot be empty!"
        if key in self.settings:
            return f"❌ Operation Failed: Setting '{key}' already exists!"
        self.settings[key] = value
        self._save_settings()
        return f"✅ Success: '{key}' configured to '{value}'."

    def update_setting(self, key, value):
        key, value = str(key).strip().lower(), str(value).strip().lower()
        if key in self.settings:
            self.settings[key] = value
            self._save_settings()
            return f"🔄 Success: '{key}' updated to '{value}'."
        return f"❌ Error: '{key}' not found. Cannot update."

    def delete_setting(self, key):
        key = str(key).strip().lower()
        if key in self.settings:
            del self.settings[key]
            self._save_settings()
            return f"🗑️ Success: '{key}' removed from configurations."
        return f"❌ Error: '{key}' does not exist."

    def view_settings(self):
        if not self.settings:
            return "\n📁 Profile Status: Empty Configuration."
        output = "\n🛠️ Current System Configuration:\n" + "="*35 + "\n"
        for key, value in self.settings.items():
            output += f" 🔹 {key.upper()}: {value}\n"
        return output

# --- Interactive Command Line Menu ---
def main():
    config = ConfigManager()
    
    while True:
        print("\n" + "="*40)
        print("⚙️  CONFIGCRAFT: CLI SETTINGS MANAGER")
        print("="*40)
        print("1. ➕ Add New Setting")
        print("2. 🔄 Update Existing Setting")
        print("3. 🗑️ Delete a Setting")
        print("4. 📋 View All Settings")
        print("5. 🚪 Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            key = input("Enter Setting Name (Key): ")
            value = input("Enter Value: ")
            print("\n" + config.add_setting(key, value))
            
        elif choice == '2':
            key = input("Enter Setting Name to Update: ")
            value = input("Enter New Value: ")
            print("\n" + config.update_setting(key, value))
            
        elif choice == '3':
            key = input("Enter Setting Name to Delete: ")
            print("\n" + config.delete_setting(key))
            
        elif choice == '4':
            print(config.view_settings())
            
        elif choice == '5':
            print("\n👋 Exiting ConfigCraft. Goodbye!")
            sys.exit()
            
        else:
            print("\n⚠️ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
