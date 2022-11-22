# Excel-to-vcf
Converting Excel Contacts to VCF file.

You need pandas installed (with openpyxl installed for reading xlsx files)


## Usage
- You just need an excel file with a "Name" and "Contacts" column.
- pass a filepath, output filename, sheet name to the function.
- run

### Edit
If you need to add more contact details change the columns read in line `name_contact` variable, create variables for them like the  `name` and `contact` vars then add them to the `vcard` variable

### Reference
https://en.wikipedia.org/wiki/VCard