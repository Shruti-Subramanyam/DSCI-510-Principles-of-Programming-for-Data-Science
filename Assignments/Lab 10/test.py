import pytest

try:
    import glob
    import importlib

    script_path = glob.glob("./lab10.py")[0]
    module_path = script_path[2:-3]
    module = importlib.import_module(module_path)
except Exception:
    raise Exception(
        "No script is available. Please follow the assignment instructions."
    )

try:
    parse_university_data = module.parse_university_data
    predict_name_attributes = module.predict_name_attributes
    parse_xml_data = module.parse_xml_data
except Exception:
    raise Exception("Please ensure all required classes have been implemented.")


parse_university_data_url1 = (
    "http://universities.hipolabs.com/search?country=United+States"
)
parse_university_data_url2 = "http://universities.hipolabs.com/search?country=India"
parse_university_data_url3 = "http://universities.hipolabs.com/search?country=China"


@pytest.mark.parametrize(
    "url, state_name, ans",
    [
        (
            parse_university_data_url1,
            "California",
            [
                {
                    "state-province": "California",
                    "country": "United States",
                    "web_pages": ["http://www.valleycollege.edu"],
                    "alpha_two_code": "US",
                    "name": "San Bernardino Valley College",
                    "domains": ["valleycollege.edu"],
                },
                {
                    "country": "United States",
                    "domains": ["sdcity.edu", "student.sdccd.edu"],
                    "state-province": "California",
                    "web_pages": ["http://www.sdcity.edu/"],
                    "alpha_two_code": "US",
                    "name": "San Diego City College",
                },
                {
                    "state-province": "California",
                    "country": "United States",
                    "domains": ["sdmesa.edu", "student.sdccd.edu"],
                    "alpha_two_code": "US",
                    "name": "San Diego Mesa College",
                    "web_pages": ["http://www.sdmesa.edu/"],
                },
                {
                    "state-province": "California",
                    "country": "United States",
                    "domains": ["sdmiramar.edu", "student.sdccd.edu"],
                    "web_pages": ["http://www.sdmiramar.edu/"],
                    "name": "San Diego Miramar College",
                    "alpha_two_code": "US",
                },
                {
                    "state-province": "California",
                    "country": "United States",
                    "name": "Academy of Art University",
                    "domains": ["academyart.edu", "art.edu"],
                    "web_pages": ["https://www.academyart.edu/"],
                    "alpha_two_code": "US",
                },
            ],
        ),
        (
            parse_university_data_url2,
            "Assam",
            [
                {
                    "state-province": "Assam",
                    "alpha_two_code": "IN",
                    "country": "India",
                    "web_pages": ["http://www.aau.ac.in/"],
                    "name": "Assam Agricultural University",
                    "domains": ["aau.ac.in"],
                },
                {
                    "domains": ["assamuniversity.nic.in"],
                    "country": "India",
                    "web_pages": ["http://www.assamuniversity.nic.in/"],
                    "name": "Assam University",
                    "state-province": "Assam",
                    "alpha_two_code": "IN",
                },
                {
                    "country": "India",
                    "state-province": "Assam",
                    "web_pages": ["http://www.iimtrichy.ac.in/"],
                    "alpha_two_code": "IN",
                    "domains": ["iiitg.ac.in"],
                    "name": "Indian Institute of Information Technology, Guwahati",
                },
                {
                    "country": "India",
                    "domains": ["iitg.ernet.in", "iitg.ac.in"],
                    "web_pages": [
                        "http://www.iitg.ernet.in/",
                        "http://www.iitg.ac.in/",
                    ],
                    "state-province": "Assam",
                    "name": "Indian Institute of Technology, Guwahati",
                    "alpha_two_code": "IN",
                },
                {
                    "state-province": "Assam",
                    "domains": ["nits.ac.in"],
                    "name": "National Institute of Technology Silchar",
                    "web_pages": ["http://www.nits.ac.in/"],
                    "alpha_two_code": "IN",
                    "country": "India",
                },
            ],
        ),
    ],
)
def test_parse_university_data(url, state_name, ans):
    assert parse_university_data(url, state_name) == ans


@pytest.mark.parametrize(
    "url, customer_id, ans",
    [
        (
            "CustomerOrdersInNameSpace.xml",
            "GREAL",
            {
                "customer_details": {
                    "CompanyName": "Great Lakes Food Market",
                    "ContactName": "Howard Snyder",
                    "ContactTitle": "Marketing Manager",
                    "Phone": "(503) 555-7555",
                    "Address": "2732 Baker Blvd.",
                    "City": "Eugene",
                    "Region": "OR",
                    "PostalCode": "97403",
                    "Country": "USA",
                },
                "order_details": [
                    {
                        "EmployeeID": "6",
                        "OrderDate": "1997-05-06T00:00:00",
                        "RequiredDate": "1997-05-20T00:00:00",
                    },
                    {
                        "EmployeeID": "8",
                        "OrderDate": "1997-07-04T00:00:00",
                        "RequiredDate": "1997-08-01T00:00:00",
                    },
                    {
                        "EmployeeID": "1",
                        "OrderDate": "1997-07-31T00:00:00",
                        "RequiredDate": "1997-08-28T00:00:00",
                    },
                    {
                        "EmployeeID": "4",
                        "OrderDate": "1997-07-31T00:00:00",
                        "RequiredDate": "1997-08-28T00:00:00",
                    },
                    {
                        "EmployeeID": "6",
                        "OrderDate": "1997-09-04T00:00:00",
                        "RequiredDate": "1997-10-02T00:00:00",
                    },
                    {
                        "EmployeeID": "3",
                        "OrderDate": "1997-09-25T00:00:00",
                        "RequiredDate": "1997-10-23T00:00:00",
                    },
                    {
                        "EmployeeID": "4",
                        "OrderDate": "1998-01-06T00:00:00",
                        "RequiredDate": "1998-02-03T00:00:00",
                    },
                    {
                        "EmployeeID": "3",
                        "OrderDate": "1998-03-09T00:00:00",
                        "RequiredDate": "1998-04-06T00:00:00",
                    },
                    {
                        "EmployeeID": "3",
                        "OrderDate": "1998-04-07T00:00:00",
                        "RequiredDate": "1998-05-05T00:00:00",
                    },
                    {
                        "EmployeeID": "4",
                        "OrderDate": "1998-04-22T00:00:00",
                        "RequiredDate": "1998-05-20T00:00:00",
                    },
                    {
                        "EmployeeID": "4",
                        "OrderDate": "1998-04-30T00:00:00",
                        "RequiredDate": "1998-06-11T00:00:00",
                    },
                ],
            },
        ),
    ],
)
def test_parse_xml_data(url, customer_id, ans):
    assert parse_xml_data(url, customer_id) == ans
    with pytest.raises(Exception):
        parse_xml_data(url, "non_existent_id")


@pytest.mark.parametrize(
    "file_name, ans",
    [
        (
            "test1.txt",
            [
                {
                    "Name": "Matt",
                    "Gender": "Male",
                    "Nationalities": ["AU", "CA", "GB", "NZ", "US"],
                    "Age": 51,
                },
                {
                    "Age": 50,
                    "Gender": "Male",
                    "Name": "Jevan",
                    "Nationalities": ["JM", "KE", "MY", "SQ", "TT"],
                },
                {
                    "Age": 60,
                    "Name": "Lionel",
                    "Nationalities": ["BE", "CH", "CM", "FR", "SQ"],
                    "Gender": "Male",
                },
                {
                    "Name": "Cristiano",
                    "Nationalities": ["AO", "BR", "IT", "PT", "TN"],
                    "Age": 48,
                    "Gender": "Male",
                },
                {
                    "Name": "Jesus",
                    "Age": 57,
                    "Gender": "Male",
                    "Nationalities": ["CO", "ES", "MX", "PE", "VE"],
                },
            ],
        ),
        (
            "test2.txt",
            [
                {
                    "Age": 44,
                    "Gender": "Female",
                    "Nationalities": ["AU", "CA", "GB", "NZ", "US"],
                    "Name": "carly",
                },
                {
                    "Age": 64,
                    "Gender": "Male",
                    "Name": "Joe",
                    "Nationalities": ["GB", "HK", "IE", "LB", "US"],
                },
                {
                    "Gender": "Male",
                    "Name": "Brad",
                    "Age": 60,
                    "Nationalities": ["AU", "CA", "GB", "NZ", "US"],
                },
                {
                    "Name": "Harry",
                    "Gender": "Male",
                    "Age": 73,
                    "Nationalities": ["AU", "GB", "ID", "NL", "NZ"],
                },
            ],
        ),
    ],
)
def test_predict_name_attributes(file_name, ans):
    assert predict_name_attributes(file_name) == ans
