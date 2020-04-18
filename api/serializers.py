from rest_framework import serializers
from ..models import Subject

class testSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = testSequence
        fields = ['name']

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['name', 'celltechnology', 'cellmanufacturer', 'numberofcells', 'numberofcellsinseries', 'numberofseriesstrings', 'numberofdiodes', 'productlength', 'productwidth', 'productweight', 'superstratetype', 'superstratemanufacturer', 'substratetype', 'substratemanufacturer', 'frametype', 'frameadhesive', 'encapsulatetype', 'encapsulantmanufacturer', 'junctionboxtype', 'junctionboxymanufacturer']

class performancedata(serializers.ModelSerializer):
    class Meta:
        model = testSequence
        fields = ['maxsystemvoltage', 'voc', 'isc', 'vmp', 'imp', 'pmp', 'ff', 'modelnumber', 'sequenceid']

class testStandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = testSequence
        fields = ['name', 'description', 'publisheddate']

class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = testSequence
        fields = ['name', 'description', 'isfirequired', 'fifrequency', 'standardid']

class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = testSequence
        fields = ['name', 'type']

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = testSequence
        fields = ['address1', 'address2', 'city', 'state', 'postalcode', 'country', 'phonenumber', 'faxnumber', 'clientid']

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = testSequence
        fields = ['firstname', 'lastname', 'middlename', 'jobtitle', 'email', 'officephone', 'cellphone', 'prefix', 'clientid']

class certificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = testSequence
        fields = ['reportnumber', 'issuedate', 'userID', 'standardid', 'locationid', 'modelNumber']
