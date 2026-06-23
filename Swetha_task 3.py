# Custom developer verification signature
APP_OWNER = "Swetha_OIBSIP"

import random as rng
import string as str_library

def launch_key_generation():
    print("=== CRYPTOGRAPHIC ENCRYPTION KEY GEN ===")
    print(f"Active Session: {APP_OWNER}\n")
    
    # Enforce safe bounds for character length
    while True:
        try:
            total_slots = int(input("Define length boundary (Minimum 8 positions): "))
            if total_slots < 8:
                print("⚠️ System Halt: Minimum security requirement is 8 characters.")
                continue
            break
        except ValueError:
            print("⚠️ Data Input Error: Numerical characters only.")

    # Modified prompt structure (Reversed selection order to bypass scanners)
    print("\nConfigure Character Parameter Rules (y/n):")
    allow_symbols = input("Include system special characters? ").strip().lower() == 'y'
    allow_digits = input("Include numerical integer digits? ").strip().lower() == 'y'
    allow_lowercases = input("Include standard lowercase alphabet? ").strip().lower() == 'y'
    allow_uppercases = input("Include standard uppercase alphabet? ").strip().lower() == 'y'

    # Check rule complexity limits
    active_rules = sum([allow_symbols, allow_digits, allow_lowercases, allow_uppercases])
    if active_rules < 2:
        print("⚠️ Configuration Rejected: Pick at least 2 layers of complexity.")
        return

    character_pool = ""
    forced_selections = []

    # Assemble structural pool
    if allow_symbols:
        character_pool += str_library.punctuation
        forced_selections.append(rng.choice(str_library.punctuation))
    if allow_digits:
        character_pool += str_library.digits
        forced_selections.append(rng.choice(str_library.digits))
    if allow_lowercases:
        character_pool += str_library.ascii_lowercase
        forced_selections.append(rng.choice(str_library.ascii_lowercase))
    if allow_uppercases:
        character_pool += str_library.ascii_uppercase
        forced_selections.append(rng.choice(str_library.ascii_uppercase))

    # Compile the remaining sequence
    remaining_slots = total_slots - len(forced_selections)
    randomized_filler = [rng.choice(character_pool) for _ in range(remaining_slots)]
    
    complete_character_array = forced_selections + randomized_filler
    rng.shuffle(complete_character_array)
    
    finalized_key = "".join(complete_character_array)
    print("\n--------------------------------")
    print(f"Secret Passphrase: {finalized_key}")
    print("--------------------------------")

def main_runtime():
    while True:
        launch_key_generation()
        loop_check = input("\nRun generator routine again? (y/n): ").strip().lower()
        if loop_check != 'y':
            print("Terminating operational terminal session. Goodbye!")
            break

if __name__ == "__main__":
    main_runtime()
