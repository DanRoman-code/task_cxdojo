from django import forms


class UploadFilesForm(forms.Form):
    upload_csv_file = forms.FileField(label='select csv_file', required=True)
    upload_xml_file = forms.FileField(label='select xml file', required=True)
