#Importing necessary libraries:
from gentopia.tools.basetool import * 
#Importing for making HTTP requests:
import urllib.request
#For parsing JSON responses:
import json
from typing import Any, Optional, Type

class CurrencyConversionArgs(BaseModel):
    #source_currency: the currency I am converting from:
    source_currency: str
    #target_currency: the currency I am converting to:
    target_currency: str
    #conversion_amount: the amount I want to convert from source_currency to target_currency:
    conversion_amount: float

class CurrencyConversion(BaseTool):
    """A Tool for converting currency using Fixer.io API Call."""
    
    name = "currency_converter"
    description = "Converting an amount from one currency to another using Fixer.io."

    args_schema: Optional[Type[BaseModel]] = CurrencyConversionArgs

    def _run(self, source_currency: str, target_currency: str, conversion_amount: float) -> str:
        #My Fixer.io API key:
        fixer_api_key = 'be97c27ab93e2d53b57f662eb6f9c86d'
        #The URL for the Fixer.io API endpoint to get the current exchange rate:
        api_url = f"http://data.fixer.io/api/latest?access_key={fixer_api_key}&symbols={source_currency},{target_currency}"
        try:
            #Making an HTTP request to the Fixer.io API:
            with urllib.request.urlopen(api_url) as api_response:
                #Parsing the JSON response:
                response_data = json.loads(api_response.read().decode())
                #Checking if the API request was successful:
                if response_data['success']:
                    #Extracting the exchange rates from the response:
                    rate_for_source = response_data['rates'][source_currency]
                    rate_for_target = response_data['rates'][target_currency]
                    #Calculating the conversion result:
                    final_conversion_result = (conversion_amount / rate_for_source) * rate_for_target
                    #Returning the converted result in correct format as a string:
                    return f"{conversion_amount} {source_currency} is approximately equal to {final_conversion_result:.2f} {target_currency}"
                else:
                    #Handling errors for invalid API key or unsupported currency:
                    detailed_error_info = response_data.get('error', {}).get('info', 'No additional error info provided.')
                    return f"Failed to convert from {source_currency} to {target_currency}. Error: {detailed_error_info}"
        except Exception as error_encountered:
            #Rasing an exception for any error occuring during the HTTP request or parsing the JSON:
            return f"An error occurred during the conversion: {str(error_encountered)}"

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    #Creating an instance of the CurrencyConversion and converting a sample i.e 100 USD to EUR:
    converter_tool = CurrencyConversion()
    print(converter_tool._run('USD', 'INR', 100))
