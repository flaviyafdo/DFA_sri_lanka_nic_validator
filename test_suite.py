"""
Comprehensive Test Suite for Sri Lankan NIC Validator
Tests various edge cases and real-world scenarios
"""

import sys
from nic_validator import NICValidator


class TestNICValidator:
    def __init__(self):
        self.validator = NICValidator()
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
    
    def test_case(self, nic, expected_valid, description, expected_gender=None):
        """Run a single test case"""
        self.total_tests += 1
        
        is_valid, message, details = self.validator.validate(nic)
        test_passed = (is_valid == expected_valid)
        
        # Additional gender check if specified
        if expected_gender and is_valid:
            gender_match = details.get('gender', '').upper() == expected_gender.upper()
            test_passed = test_passed and gender_match
        
        status = "✓" if test_passed else "✗"
        result = "ACCEPT" if is_valid else "REJECT"
        
        print(f"{status} Test {self.total_tests:3d}: {nic:20s} | {result:8s} | {description}")
        
        if not test_passed:
            print(f"           Expected: {'ACCEPT' if expected_valid else 'REJECT'}")
            print(f"           Got: {message}")
            self.failed_tests += 1
        else:
            self.passed_tests += 1
            if details and is_valid:
                print(f"           Gender: {details.get('gender', 'N/A')}, "
                      f"Year: {details.get('birth_year', 'N/A')}, "
                      f"Day: {details.get('day_of_year', 'N/A')}")
        print()
    
    def run_all_tests(self):
        """Run comprehensive test suite"""
        print("\n" + "="*100)
        print(" "*30 + "NIC VALIDATOR TEST SUITE")
        print("="*100 + "\n")
        
        # Category 1: Valid Old Format NICs (Male)
        print("="*100)
        print("CATEGORY 1: VALID OLD FORMAT - MALE")
        print("="*100)
        self.test_case("901234567V", True, "1990 birth, Male, standard format", "Male")
        self.test_case("850234567X", True, "1985 birth, Male, X suffix", "Male")
        self.test_case("750100123V", True, "1975 birth, Male, Jan 1", "Male")
        self.test_case("000010001V", True, "2000 birth, Male, Jan 1", "Male")
        self.test_case("990366789V", True, "1999 birth, Male, Dec 31 (leap year)", "Male")
        self.test_case("960152345V", True, "1996 birth, Male, Jan 15", "Male")
        self.test_case("720321456V", True, "1972 birth, Male, Nov 17", "Male")
        
        # Category 2: Valid Old Format NICs (Female)
        print("="*100)
        print("CATEGORY 2: VALID OLD FORMAT - FEMALE")
        print("="*100)
        self.test_case("885501234V", True, "1988 birth, Female (day=501)", "Female")
        self.test_case("925650123V", True, "1992 birth, Female (day=565)", "Female")
        self.test_case("708661234V", True, "1970 birth, Female, Dec 31 (day=866)", "Female")
        self.test_case("015201234V", True, "2001 birth, Female (day=520)", "Female")
        self.test_case("825725678X", True, "1982 birth, Female (day=725)", "Female")
        
        # Category 3: Valid New Format NICs (Male)
        print("="*100)
        print("CATEGORY 3: VALID NEW FORMAT - MALE")
        print("="*100)
        self.test_case("199001012345", True, "1990 birth, Male, 12-digit", "Male")
        self.test_case("198503456789", True, "1985 birth, Male", "Male")
        self.test_case("200001001234", True, "2000 birth, Male, Jan 1", "Male")
        self.test_case("197536612345", True, "1975 birth, Male, Dec 31 (leap year)", "Male")
        self.test_case("202015023456", True, "2020 birth, Male", "Male")
        
        # Category 4: Valid New Format NICs (Female)
        print("="*100)
        print("CATEGORY 4: VALID NEW FORMAT - FEMALE")
        print("="*100)
        self.test_case("199050112345", True, "1990 birth, Female (day=501)", "Female")
        self.test_case("200156789012", True, "2001 birth, Female (day=567)", "Female")
        self.test_case("198586612345", True, "1985 birth, Female (day=866)", "Female")
        self.test_case("202052034567", True, "2020 birth, Female (day=520)", "Female")
        
        # Category 5: Invalid Length
        print("="*100)
        print("CATEGORY 5: INVALID LENGTH")
        print("="*100)
        self.test_case("12345", False, "Too short")
        self.test_case("123456789", False, "9 digits only (missing suffix)")
        self.test_case("12345678901", False, "11 digits (invalid length)")
        self.test_case("1234567890123", False, "13 digits (too long)")
        self.test_case("", False, "Empty string")
        
        # Category 6: Invalid Characters
        print("="*100)
        print("CATEGORY 6: INVALID CHARACTERS")
        print("="*100)
        self.test_case("99012345678A", False, "Invalid suffix (A instead of V/X)")
        self.test_case("99O12345678V", False, "Letter O instead of digit 0")
        self.test_case("990123456@V", False, "Special character @")
        self.test_case("ABCDEFGHIJ", False, "All letters")
        self.test_case("990123 5678V", False, "Contains space")
        self.test_case("99-12345678V", False, "Contains hyphen")
        
        # Category 7: Invalid Day Count
        print("="*100)
        print("CATEGORY 7: INVALID DAY COUNT")
        print("="*100)
        self.test_case("990000123V", False, "Day count 000 (invalid)")
        self.test_case("994001234V", False, "Day count 400 (too high for male)")
        self.test_case("995001234V", False, "Day count 500 (boundary)")
        self.test_case("999001234V", False, "Day count 900 (too high for female)")
        self.test_case("999991234V", False, "Day count 999 (invalid)")
        self.test_case("199000012345", False, "New format - day 000")
        self.test_case("199090012345", False, "New format - day 900")
        
        # Category 8: Edge Cases
        print("="*100)
        print("CATEGORY 8: EDGE CASES")
        print("="*100)
        self.test_case("000011234V", True, "Year 00 (2000)", "Male")
        self.test_case("250010001V", True, "Year 25 (2025)", "Male")
        self.test_case("990010001v", True, "Lowercase 'v' suffix (should accept)", "Male")
        self.test_case("990010001x", True, "Lowercase 'x' suffix (should accept)", "Male")
        self.test_case("119901012345", True, "Year 1199 (unusual but valid format)", "Male")
        self.test_case("399901012345", True, "Year 3999 (unusual but valid format)", "Male")
        
        # Category 9: Real-world Examples
        print("="*100)
        print("CATEGORY 9: REALISTIC SRI LANKAN NIC EXAMPLES")
        print("="*100)
        self.test_case("912345678V", True, "Typical 1991 male NIC", "Male")
        self.test_case("886501234V", True, "Typical 1988 female NIC", "Female")
        self.test_case("199112345678", True, "New format 1991 male", "Male")
        self.test_case("198856712345", True, "New format 1988 female", "Female")
        self.test_case("757251234V", True, "1975 female NIC (day=725)", "Female")
        self.test_case("651234567X", True, "1965 male NIC with X", "Male")
        
        # Category 10: Boundary Testing
        print("="*100)
        print("CATEGORY 10: BOUNDARY VALUE TESTING")
        print("="*100)
        self.test_case("900010001V", True, "Day 001 - January 1st", "Male")
        self.test_case("903661234V", True, "Day 366 - December 31st (leap)", "Male")
        self.test_case("905011234V", True, "Day 501 - Female January 1st", "Female")
        self.test_case("908661234V", True, "Day 866 - Female December 31st", "Female")
        self.test_case("190000012345", False, "New format - day 000")
        self.test_case("190036712345", False, "New format - day 367 (invalid)")
        
        # Print summary
        print("\n" + "="*100)
        print("TEST SUMMARY")
        print("="*100)
        print(f"Total Tests: {self.total_tests}")
        print(f"Passed: {self.passed_tests} ({(self.passed_tests/self.total_tests*100):.1f}%)")
        print(f"Failed: {self.failed_tests} ({(self.failed_tests/self.total_tests*100):.1f}%)")
        print("="*100 + "\n")
        
        return self.failed_tests == 0


def main():
    """Run the test suite"""
    tester = TestNICValidator()
    success = tester.run_all_tests()
    
    if success:
        print("✓ All tests passed!")
        sys.exit(0)
    else:
        print("✗ Some tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()