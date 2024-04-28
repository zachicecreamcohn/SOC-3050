import requests

def get_median_household_income(fips_code, api_key):
    # Base URL for the Census API
    base_url = 'https://api.census.gov/data/2021/acs/acs1'

    # Determine the level of detail based on the length of the FIPS code
    if len(fips_code) == 2:  # State level
        geog_level = "state"
        url = f"{base_url}?get=B19013_001E&for=state:{fips_code}&key={api_key}"
    elif len(fips_code) == 5:  # County level
        geog_level = "county"
        state_code = fips_code[:2]
        url = f"{base_url}?get=B19013_001E&for=county:{fips_code[2:]}&in=state:{state_code}&key={api_key}"
    elif len(fips_code) >= 6:  # Tract level
        geog_level = "tract"
        state_code = fips_code[:2]
        county_code = fips_code[2:5]
        url = f"{base_url}?get=B19013_001E&for=tract:{fips_code[5:]}&in=state:{state_code}+county:{county_code}&key={api_key}"

    # Send the request to the Census API
    response = requests.get(url)

    if response.status_code == 200:
        # Parse and return the JSON response
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return "Error decoding JSON response."
    else:
        # Return error with status code and response text for debugging
        return f"Failed to retrieve data: status code {response.status_code}, response text: '{response.text}'"

# Example usage
test_fips = '17031150502'
api_key = 'ac3430b99cde45b2fca0224a8f714d5db5016c71'
data = get_median_household_income(test_fips, api_key)
print(data)
