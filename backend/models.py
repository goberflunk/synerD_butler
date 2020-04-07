from django.db import models

# Create your models here.
class testSequence(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=25)
    celltechnology = models.CharField(max_length=25)
    cellmanufacturer = models.CharField(max_length=25)
    numberofcells = models.CharField(max_length=25)
    numberofcellsinseries = models.CharField(max_length=25)
    numberofseriesstrings = models.CharField(max_length=25)
    numberofdiodes = models.CharField(max_length=25)
    productlength = models.CharField(max_length=25)
    productwidth = models.CharField(max_length=25)
    productweight = models.CharField(max_length=25)
    superstratetype = models.CharField(max_length=25)
    superstratemanufacturer = models.CharField(max_length=25)
    substratetype = models.CharField(max_length=25)
    substratemanufacturer = models.CharField(max_length=25)
    frametype = models.CharField(max_length=25)
    frameadhesive = models.CharField(max_length=25)
    encapsulatetype = models.CharField(max_length=25)
    encapsulantmanufacturer = models.CharField(max_length=25)
    junctionboxtype = models.CharField(max_length=25)
    junctionboxymanufacturer = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class performancedata(models.Model):
    maxsystemvoltage = models.CharField(max_length=25)
    voc = models.CharField(max_length=25)
    isc = models.CharField(max_length=25)
    vmp = models.CharField(max_length=25)
    imp = models.CharField(max_length=25)
    pmp = models.CharField(max_length=25)
    ff = models.CharField(max_length=25)
    modelnumber = models.ForeignKey(product,  on_delete=models.CASCADE)
    sequenceid = models.ForeignKey(testSequence, on_delete=models.CASCADE)

    def __str__(self):
        return self.maxsystemvoltage

class testStandard(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=25)
    publisheddate = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class service(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=25)
    isfirequired = models.CharField(max_length=25)
    fifrequency = models.CharField(max_length=25)
    standardid = models.ForeignKey(testStandard, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class client(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class location(models.Model):
    address1 = models.CharField(max_length=25)
    address2 = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    postalcode = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=25)
    faxnumber = models.CharField(max_length=25)
    clientid = models.ForeignKey(client, on_delete=models.CASCADE)

    def __str__(self):
        return self.address1

class user(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    middlename = models.CharField(max_length=25)
    jobtitle = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    officephone = models.CharField(max_length=25)
    cellphone = models.CharField(max_length=25)
    prefix = models.CharField(max_length=25)
    clientid = models.ForeignKey(client, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname

class certificate(models.Model):
    reportnumber = models.CharField(max_length=25)
    issuedate = models.CharField(max_length=25)
    userID = models.ForeignKey(user, on_delete=models.CASCADE)
    standardid = models.ForeignKey(testStandard, on_delete=models.CASCADE)
    locationid = models.ForeignKey(location, on_delete=models.CASCADE)
    modelNumber = models.ForeignKey(product, on_delete=models.CASCADE)

    def __str__(self):
        return self.reportnumber
