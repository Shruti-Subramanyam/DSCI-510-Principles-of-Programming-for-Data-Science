from typing import List


def generate_frequency_map(file_name: str) -> List[int]:
    List = [0] * 10
    try:
        f = open(file_name, "r")
        for i in f:
            count = int(i.strip())
            if 0 <= count <= 9:
                List[count] += 1
    except Exception:
        raise
    finally:
        f.close()
    return List


def split_by_delimiter(some_string: str, delimiter: str) -> list:
    try:
        output = list()
        string = str()
        if isinstance(some_string, str) and isinstance(delimiter, str):
            for character in some_string:
                if character is not delimiter:
                    string = string + character
                else:
                    output.append(string)
                    string = ""
            output.append(string)
            return output
        else:
            raise ValueError("Invalid Input")
    except ValueError:
        raise


def palindrome_finder(file_name: str):
    try:
        file_input = open(file_name, "r")
        file_output = open(f"palindrome_{file_name}", "w")
        # for i in file_input:
        split_by_delimiter(file_input.read(), " ")
        
    except Exception:
        raise
    finally:
        file_input.close()
        file_output.close()


palindrome_finder("sentences_3.txt")


def file_extension(file_name: str):
    file_pdf = open(f"pdf_{file_name}", "w")
    file_doc = open(f"doc_{file_name}", "w")
    file_txt = open(f"txt_{file_name}", "w")
    try:
        file_input = open(file_name, "r")
        for i in file_input:
            extension = split_by_delimiter(i, ".")[-1]
            if extension == "pdf":
                file_pdf.write(f"{i}\n")
            if extension == "doc":
                file_doc.write(f"{i}\n")
            if extension == "txt":
                file_txt.write(f"{i}\n")
    except Exception:
        raise
    finally:
        file_input.close()
        file_pdf.close()
        file_doc.close()
        file_txt.close()


file_extension("extensions_1.txt")