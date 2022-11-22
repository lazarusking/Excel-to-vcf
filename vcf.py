# %%
import pandas as pd


def vcf_creator(file_path, output_filename="output.vcf", sheet=0):
    data = pd.read_excel(file_path, sheet_name=sheet)
    data.columns = data.columns.str.strip()
    name_contact = data[["Name", "Contacts"]]
    # name_contact["Contacts"] = name_contact["Contacts"].apply(
    #     lambda x: x.split("/")[0])
    # name_contact = pd.DataFrame(
    #     [row for row in zip(name_contact["Name"], name_contact["Contacts"])])

    begin = "BEGIN:VCARD\nVERSION:2.1\n"
    vcard = ""

    for i in name_contact.index:
        name = name_contact["Name"][i]
        contact = name_contact["Contacts"][i].split("/")[0]
        vcard += f"{begin}N:{name}\nTEL;CELL:{contact}\nEND:VCARD\n"
    with open(output_filename, "w") as file:
        file.write(vcard)
    print(vcard)


vcf_creator("/home/accel/some/directory/file.xlsx",
            "contacts.vcf", "sheet name")

# %%
