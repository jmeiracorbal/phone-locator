from phonenumbers import (
    carrier, geocoder, timezone, 
    parse, format_number, 
    format_number_for_mobile_dialing, 
    is_valid_number, is_possible_number,
    number_type,
    PhoneNumberFormat,
    PhoneNumberType,
    region_code_for_number
)

from constants import Wh, Gr, Re

def track_phone():
    """Find phone numbers information"""
    print(f"\n {Wh}Enter phone number information:")
    
    country_code = input(f" {Wh} Country Code {Gr} (without +) {Wh}: {Gr}")
    phone_number = input(f" {Wh} Phone Number {Gr}: {Wh}: {Gr}")
    
    # country code and number
    full_number = "+" + country_code + phone_number
    
    try:
        parsed_number = parse(full_number)
        region_code = region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid = is_valid_number(parsed_number)
        is_possible = is_possible_number(parsed_number)
        formatted_number = format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = format_number_for_mobile_dialing(parsed_number, region_code or "US", with_formatting=True)
        num_type = number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
        print(f"\n {Wh}Full Number         :{Gr} {full_number}")
        print(f" {Wh}Location             :{Gr} {location}")
        print(f" {Wh}Region Code          :{Gr} {region_code}")
        print(f" {Wh}Timezone             :{Gr} {timezoneF}")
        print(f" {Wh}Operator             :{Gr} {jenis_provider}")
        print(f" {Wh}Valid number         :{Gr} {is_valid}")
        print(f" {Wh}Possible number      :{Gr} {is_possible}")
        print(f" {Wh}International format :{Gr} {formatted_number}")
        print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
        print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
        print(f" {Wh}E.164 format         :{Gr} {format_number(parsed_number, PhoneNumberFormat.E164)}")
        print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
        print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
        
        if num_type == PhoneNumberType.MOBILE:
            print(f" {Wh}Type                 :{Gr} This is a mobile number")
        elif num_type == PhoneNumberType.FIXED_LINE:
            print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
        else:
            print(f" {Wh}Type                 :{Gr} This is another type of number")
        
        national_format = format_number(parsed_number, PhoneNumberFormat.NATIONAL)
        print(f" {Wh}National format      :{Gr} {national_format}")
        
        is_portable = is_possible_number(parsed_number)
        print(f" {Wh}Portable number      :{Gr} {is_portable}")
        
        timezone_info = timezone.time_zones_for_number(parsed_number)
        if timezone_info:
            print(f" {Wh}Best calling time    :{Gr} Check local time in {', '.join(timezone_info)}")
        
        if num_type == PhoneNumberType.PREMIUM_RATE:
            print(f" {Wh}Cost type            :{Gr} Premium rate (expensive)")
        elif num_type == PhoneNumberType.TOLL_FREE:
            print(f" {Wh}Cost type            :{Gr} Toll-free (free to call)")
        else:
            print(f" {Wh}Cost type            :{Gr} Standard rate")
            
    except Exception as e:
        print(f"{Re}Error: {e}")
