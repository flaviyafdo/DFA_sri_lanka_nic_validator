"""
Sri Lankan NIC (National Identity Card) Number Validator
Using Deterministic Finite Automaton (DFA)

Author: Automata Theory Project
Date: December 2025

NIC Format Rules:
1. Old Format (Before 2016): 9 digits + V/X
   - Format: XXXXXXXXXV or XXXXXXXXX X
   - Example: 199012345678V, 850234567X
   
2. New Format (After 2016): 12 digits
   - Format: XXXXXXXXXXXX
   - Example: 199901234567

Encoding Rules:
- Old Format: Birth year (first 2 digits) + Days from Jan 1 (next 3 digits) + Serial (next 4 digits) + V/X
- New Format: Birth year (first 4 digits) + Days from Jan 1 (next 3 digits) + Serial (next 4 digits) + Check digit

Days Encoding:
- Male: Days from Jan 1 (001-366)
- Female: Days + 500 (501-866)
"""

class NICValidator:
    def __init__(self):
        """Initialize the NIC Validator DFA"""
        # Define states for the DFA
        self.states = {
            'q0': 'Start State',
            'q1': 'First digit read (Old format)',
            'q2': 'Second digit read (Old format)',
            'q3': 'Third digit read (Day counter starts)',
            'q4': 'Fourth digit read',
            'q5': 'Fifth digit read (Day counter complete)',
            'q6': 'Sixth digit read (Serial starts)',
            'q7': 'Seventh digit read',
            'q8': 'Eighth digit read',
            'q9': 'Ninth digit read (Serial complete)',
            'q10': 'V or X read (Old format accepting)',
            'q11': 'New format - year digit 3',
            'q12': 'New format - year digit 4',
            'q13': 'New format - day digit 1',
            'q14': 'New format - day digit 2',
            'q15': 'New format - day digit 3',
            'q16': 'New format - serial digit 1',
            'q17': 'New format - serial digit 2',
            'q18': 'New format - serial digit 3',
            'q19': 'New format - serial digit 4',
            'q20': 'New format - check digit (Accepting)',
            'qReject': 'Reject State'
        }
        
        self.start_state = 'q0'
        self.accepting_states = {'q10', 'q20'}
        self.current_state = self.start_state
        
        # Store the NIC being validated
        self.nic_input = ""
        self.validation_details = {}
    
    def reset(self):
        """Reset the DFA to start state"""
        self.current_state = self.start_state
        self.nic_input = ""
        self.validation_details = {}
    
    def transition(self, symbol, position):
        """
        Define the transition function δ(state, symbol) -> next_state
        """
        state = self.current_state
        
    def transition(self, symbol, position):
        """
        Define the transition function δ(state, symbol) -> next_state
        """
        state = self.current_state
        
        # From start state - route based on predetermined format
        if state == 'q0':
            if symbol.isdigit():
                if self.validation_details.get('format') == 'new':
                    self.current_state = 'q11'  # New format path (12 digits)
                    self.validation_details['year_start'] = symbol
                else:
                    self.current_state = 'q1'  # Old format path (10 chars)
                    self.validation_details['year_start'] = symbol
            else:
                self.current_state = 'qReject'
        
        # Old format path (9 digits + V/X)
        elif state == 'q1':
            if symbol.isdigit():
                self.current_state = 'q2'
                self.validation_details['year_start'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q2':
            if symbol.isdigit():
                self.current_state = 'q3'
                self.validation_details['day_count'] = symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q3':
            if symbol.isdigit():
                self.current_state = 'q4'
                self.validation_details['day_count'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q4':
            if symbol.isdigit():
                self.current_state = 'q5'
                self.validation_details['day_count'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q5':
            if symbol.isdigit():
                self.current_state = 'q6'
                self.validation_details['serial'] = symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q6':
            if symbol.isdigit():
                self.current_state = 'q7'
                self.validation_details['serial'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q7':
            if symbol.isdigit():
                self.current_state = 'q8'
                self.validation_details['serial'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q8':
            if symbol.isdigit():
                self.current_state = 'q9'
                self.validation_details['serial'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q9':
            if symbol.upper() in ['V', 'X']:
                self.current_state = 'q10'  # Accepting state
                self.validation_details['suffix'] = symbol.upper()
            else:
                self.current_state = 'qReject'
        
        # New format path (12 digits)
        elif state == 'q11':
            if symbol.isdigit():
                self.current_state = 'q12'
                self.validation_details['year_start'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q12':
            if symbol.isdigit():
                self.current_state = 'q13'
                self.validation_details['year_start'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q13':
            if symbol.isdigit():
                self.current_state = 'q14'
                self.validation_details['year_start'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q14':
            if symbol.isdigit():
                self.current_state = 'q15'
                self.validation_details['day_count'] = symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q15':
            if symbol.isdigit():
                self.current_state = 'q16'
                self.validation_details['day_count'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q16':
            if symbol.isdigit():
                self.current_state = 'q17'
                self.validation_details['day_count'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q17':
            if symbol.isdigit():
                self.current_state = 'q18'
                self.validation_details['serial'] = symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q18':
            if symbol.isdigit():
                self.current_state = 'q19'
                self.validation_details['serial'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q19':
            if symbol.isdigit():
                self.current_state = 'q20'  # Accepting state
                self.validation_details['serial'] += symbol
            else:
                self.current_state = 'qReject'
        
        elif state == 'q20':
            if symbol.isdigit():
                # Stay in accepting state (for the last digit)
                self.validation_details['check_digit'] = symbol
            else:
                self.current_state = 'qReject'
        
        else:
            # Reject state or any other unexpected state
            self.current_state = 'qReject'
    
    def validate_semantic_rules(self):
        """
        Validate semantic rules beyond DFA structure:
        1. Day count should be valid (001-366 for male, 501-866 for female)
        2. Year should be reasonable
        """
        if not self.validation_details:
            return False, "No validation details available"
        
        try:
            day_count = int(self.validation_details.get('day_count', '0'))
            original_day_count = day_count
            
            # Check if male or female based on day count
            if 1 <= day_count <= 366:
                gender = "Male"
                actual_day = day_count
            elif 501 <= day_count <= 866:
                gender = "Female"
                actual_day = day_count - 500  # Adjust for actual day calculation
            else:
                return False, f"Invalid day count: {day_count}. Must be 001-366 (Male) or 501-866 (Female)"
            
            # Validate actual day count (considering leap years, we accept up to 366)
            if actual_day < 1 or actual_day > 366:
                return False, f"Day count out of range: {actual_day}"
            
            self.validation_details['gender'] = gender
            self.validation_details['day_of_year'] = actual_day
            self.validation_details['original_day_count'] = original_day_count
            
            # Calculate approximate birth year
            if self.validation_details['format'] == 'old':
                year_prefix = self.validation_details['year_start']
                # Assume 19xx for years before 2000, 20xx for years after
                year = int(year_prefix)
                if year >= 0 and year <= 25:
                    full_year = 2000 + year
                else:
                    full_year = 1900 + year
                self.validation_details['birth_year'] = full_year
            else:  # new format
                full_year = int(self.validation_details['year_start'])
                self.validation_details['birth_year'] = full_year
            
            return True, f"Valid NIC - Gender: {gender}, Birth Year: {self.validation_details['birth_year']}, Day: {actual_day}"
        
        except Exception as e:
            return False, f"Semantic validation error: {str(e)}"
    
    def validate(self, nic):
        """
        Main validation function
        Returns: (is_valid, message, details)
        """
        self.reset()
        self.nic_input = nic.strip().upper()
        
        # Check length first and determine format
        if len(self.nic_input) not in [10, 12]:
            return False, "Invalid NIC length. Must be 10 (old format) or 12 (new format) characters", {}
        
        # Set format based on length
        if len(self.nic_input) == 10:
            self.validation_details['format'] = 'old'
        else:  # 12
            self.validation_details['format'] = 'new'
        
        # Process each symbol through the DFA
        for i, symbol in enumerate(self.nic_input):
            self.transition(symbol, i)
            
            # Early termination if we reach reject state
            if self.current_state == 'qReject':
                return False, f"Invalid character '{symbol}' at position {i+1}", {}
        
        # Check if we ended in an accepting state
        if self.current_state not in self.accepting_states:
            return False, f"Invalid NIC format. Ended in non-accepting state: {self.current_state}", {}
        
        # Validate semantic rules
        is_semantic_valid, message = self.validate_semantic_rules()
        
        if is_semantic_valid:
            return True, message, self.validation_details
        else:
            return False, message, self.validation_details


def print_state_diagram():
    """Print ASCII representation of the state diagram"""
    print("\n" + "="*80)
    print("DFA STATE DIAGRAM FOR SRI LANKAN NIC VALIDATOR")
    print("="*80)
    print("""
OLD FORMAT PATH (9 digits + V/X):
                    digit(0-9)      digit      digit      digit      digit
    [q0] -------> [q1] -------> [q2] -------> [q3] -------> [q4] -------> [q5]
    start          |              |            |            |            |
                   Year(2)      Day(1)       Day(2)       Day(3)     Serial(1)
    
         digit      digit      digit      digit      V/X
    ---> [q6] ---> [q7] ---> [q8] ---> [q9] ---> ((q10))
        Serial(2) Serial(3) Serial(4)            ACCEPT
    
NEW FORMAT PATH (12 digits):
                    digit(0,1,2)  digit      digit      digit
    [q0] -------> [q11] -------> [q12] -----> [q13] -----> [q14]
    start          |               |            |           |
                Year(1)         Year(2)      Year(3)     Year(4)
    
         digit      digit      digit      digit      digit      digit      digit
    ---> [q15] --> [q16] ---> [q17] ---> [q18] ---> [q19] ---> [q20] ---> ((q20))
        Day(1)    Day(2)    Day(3)    Serial(1) Serial(2) Serial(3) Serial(4)+Check
                                                                            ACCEPT

ALPHABET (Σ): {0,1,2,3,4,5,6,7,8,9,V,X,v,x}
START STATE (q₀): q0
ACCEPTING STATES (F): {q10, q20}
""")
    print("="*80 + "\n")


def test_nic_validator():
    """Test the NIC validator with sample data"""
    validator = NICValidator()
    
    # Test cases with real Sri Lankan NIC patterns
    test_cases = [
        # Old format - Valid
        ("199012345678V", True, "Valid old format - Male"),
        ("850234567X", True, "Valid old format - Male"),
        ("725501234V", True, "Valid old format - Female (day > 500)"),
        ("916789012V", True, "Valid old format - Male"),
        ("990123456V", True, "Valid old format - Male"),
        
        # New format - Valid
        ("199901234567", True, "Valid new format - Male"),
        ("200156712345", True, "Valid new format - Female"),
        ("198523412345", True, "Valid new format"),
        ("202012345678", True, "Valid new format"),
        
        # Invalid cases
        ("12345", False, "Too short"),
        ("123456789012345", False, "Too long"),
        ("99012345678A", False, "Invalid suffix (should be V or X)"),
        ("19990123456", False, "Wrong length for new format"),
        ("850934567V", False, "Invalid day count (934 > 866)"),
        ("ABCDEFGHIJ", False, "Non-numeric characters"),
        ("199912345678", False, "Day count 999 is invalid"),
        ("", False, "Empty string"),
    ]
    
    print("\n" + "="*80)
    print("TESTING NIC VALIDATOR")
    print("="*80 + "\n")
    
    passed = 0
    failed = 0
    
    for nic, expected_valid, description in test_cases:
        is_valid, message, details = validator.validate(nic)
        
        # Check if result matches expectation
        test_passed = (is_valid == expected_valid)
        
        status = "✓ PASS" if test_passed else "✗ FAIL"
        result = "ACCEPT" if is_valid else "REJECT"
        
        print(f"{status} | NIC: {nic:20s} | {result:8s} | {description}")
        print(f"       Message: {message}")
        
        if details:
            print(f"       Details: {details}")
        print()
        
        if test_passed:
            passed += 1
        else:
            failed += 1
    
    print("="*80)
    print(f"TEST RESULTS: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("="*80 + "\n")


def interactive_mode():
    """Interactive mode for user input"""
    validator = NICValidator()
    
    print("\n" + "="*80)
    print("SRI LANKAN NIC VALIDATOR - INTERACTIVE MODE")
    print("="*80)
    print("\nEnter 'quit' or 'exit' to stop\n")
    
    while True:
        try:
            nic = input("Enter NIC number: ").strip()
            
            if nic.lower() in ['quit', 'exit', 'q']:
                print("\nExiting validator. Thank you!")
                break
            
            if not nic:
                print("Please enter a valid NIC number.\n")
                continue
            
            is_valid, message, details = validator.validate(nic)
            
            print("\n" + "-"*80)
            if is_valid:
                print(f"✓ RESULT: ACCEPT")
                print(f"✓ {message}")
                print(f"\nDetails:")
                print(f"  - Format: {details.get('format', 'N/A').upper()}")
                print(f"  - Birth Year: {details.get('birth_year', 'N/A')}")
                print(f"  - Gender: {details.get('gender', 'N/A')}")
                print(f"  - Day of Year: {details.get('day_of_year', 'N/A')}")
                if 'suffix' in details:
                    print(f"  - Suffix: {details.get('suffix', 'N/A')}")
            else:
                print(f"✗ RESULT: REJECT")
                print(f"✗ {message}")
            print("-"*80 + "\n")
            
        except KeyboardInterrupt:
            print("\n\nExiting validator. Thank you!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


def main():
    """Main function"""
    print("\n" + "="*80)
    print(" "*20 + "SRI LANKAN NIC VALIDATOR")
    print(" "*15 + "Using Deterministic Finite Automaton (DFA)")
    print("="*80)
    
    # Display state diagram
    print_state_diagram()
    
    # Run automated tests
    test_nic_validator()
    
    # Start interactive mode
    interactive_mode()


if __name__ == "__main__":
    main()