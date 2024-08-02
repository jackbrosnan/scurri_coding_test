import re

class UKPostcode:
    """
    Postcode pattern:

    Outward Code (e.g., "SW1A"):
        One or two letters (A-Z)
        Followed by one or two digits (0-9), optionally followed by a letter (A-Z)
    
    
    Inward Code (e.g., "1AA"):
        One digit (0-9)
        Followed by two letters (A-Z)    

    (Inward and outward code seperated by a space)

    """

    POSTCODE_REGEX = re.compile(
        r'^(?:[A-Z][A-Z][0-9][A-Z])|'
        r'(?:[A-Z][A-Z][0-9]{1,2})|'
        r'(?:[A-Z][0-9][A-Z])|'
        r'(?:[A-Z][0-9]{1,2}\s?[0-9][A-Z]{2})$', 
        re.IGNORECASE
    )

    def is_valid_postcode(postcode: str) -> bool:
        """
        Validates the format of a UK postcode.

        returns True if the postcode is valid, False otherwise.
        """

        return bool(UKPostcode.POSTCODE_REGEX.match(postcode))
    
    def format_postcode(postcode: str) -> str:
        """Format the UK postcode to the standard form with a space."""
        
        postcode = postcode.strip().upper()
        if not UKPostcode.is_valid_postcode(postcode):
            return ValueError('Invalid Postcode')
        
        if postcode[-4] != ' ':
            postcode = postcode[:-3] + ' ' + postcode[-3:]
        
        return postcode

# Example usage
if __name__ == "__main__":
    sample_postcodes = [
        "AA9A9AA", "W1A0AX", "M11AE", "B338TH", "CR26XH", "DN551PT", "G58 1SB",
        "B1 1HQ", "BX4 7SB", "E20 2AQ", "INVALID", "TKCA 1ZZ", "A00BBB",
    ]

    for code in sample_postcodes:
        print(f'Unformatted Postcode: {code}')
        print(f'Valid: {UKPostcode.is_valid_postcode(code)}')
        if UKPostcode.is_valid_postcode(code):
            print(f'Formatted Postcode: {UKPostcode.format_postcode(code)}')
        print('\n')