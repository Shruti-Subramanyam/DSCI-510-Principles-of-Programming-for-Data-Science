import requests
import xml.etree.ElementTree as ET
from typing import List


def parse_university_data(url, state_name) -> List[dict]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        university_data = response.json()
        state_data = [
            university
            for university in university_data
            if university.get("state-province") == state_name
        ]
        if not state_data:
            raise ("specified state_name does not exist")
        final_data = []
        for i in state_data:
            final_data.append(
                {
                    "state-province": i["state-province"],
                    "country": i["country"],
                    "domains": i["domains"],
                    "web_pages": i["web_pages"],
                    "alpha_two_code": i["alpha_two_code"],
                    "name": i["name"],
                }
            )
        return final_data

    except requests.exceptions.RequestException:
        raise Exception("URL cannot be accessed.")
    except KeyError:
        raise Exception("Required keys are missing in the json data")


def predict_name_attributes(file_name: str) -> List[dict]:
    final_data = []
    with open(file_name, "r") as fp:
        names = fp.read().splitlines()
    default_age = 50
    default_gender = "Female"
    default_nationality = "US"
    for name in names:
        attributes = {
            "Name": name,
            "Gender": default_gender.capitalize(),
            "Nationalities": [default_nationality],
            "Age": default_age,
        }
        age_api = f"https://api.agify.io?name={name}"
        gender_api = f"https://api.genderize.io?name={name}"
        nationality_api = f"https://api.nationalize.io?name={name}"
        try:
            age_response = requests.get(age_api).json()
            if "age" in age_response:
                attributes["Age"] = age_response["age"]
            gender_response = requests.get(gender_api).json()
            if "gender" in gender_response:
                attributes["Gender"] = gender_response["gender"].capitalize()
            nationality_response = requests.get(nationality_api).json()
            if "country" in nationality_response:
                nationalities = []
                for i in nationality_response["country"]:
                    nationalities.append(i["country_id"])
                attributes["Nationalities"] = sorted(nationalities)
        except Exception as e:
            print("Error for name", e)
        final_data.append(attributes)
    return final_data


def parse_xml_data(path, customer_id):
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        customer_details = {}
        order_details = []
        for customer in root.findall(".//Customers/Customer"):
            if customer.get("CustomerID") == customer_id:
                customer_details["CompanyName"] = customer.find("CompanyName").text
                customer_details["ContactName"] = customer.find("ContactName").text
                customer_details["ContactTitle"] = customer.find("ContactTitle").text
                customer_details["Phone"] = customer.find("Phone").text
                full_address = customer.find(".//FullAddress")
                customer_details["Address"] = full_address.find("Address").text
                customer_details["City"] = full_address.find("City").text
                customer_details["Region"] = full_address.find("Region").text
                customer_details["PostalCode"] = full_address.find("PostalCode").text
                customer_details["Country"] = full_address.find("Country").text
        if not customer_details:
            raise Exception(f"Customer ID ({customer_id}) not found")
        for order in root.findall(".//Orders/Order[CustomerID='" + customer_id + "']"):
            order_info = {
                "EmployeeID": order.find("EmployeeID").text,
                "OrderDate": order.find("OrderDate").text,
                "RequiredDate": order.find("RequiredDate").text,
            }
            order_details.append(order_info)
        result = {"customer_details": customer_details, "order_details": order_details}
        return result
    except Exception as e:
        raise e
