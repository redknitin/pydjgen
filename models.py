from django.db import models

class NameModelBase(models.Model):
	name=models.CharField(max_length=80)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.__unicode__()
	class Meta:
		abstract=True

class Country(NameModelBase):
	currency=models.CharField(max_length=80)

class Bank(NameModelBase):
	pass

class AccountType(NameModelBase):
	pass

class Account(models.Model):
	bank=models.ForeignKey('Bank')
	accountno=models.CharField(max_length=80)
	accounttype=models.ForeignKey('AccountType')
	currency=models.ForeignKey('Country')

class Party(NameModelBase):
	address=models.CharField(max_length=2000, blank=True, null=True)
	phone=models.CharField(max_length=20, blank=True, null=True)

class ChequeBook(models.Model):
	account=models.ForeignKey('Account')
	bookno=models.CharField(max_length=30)
	firstno=models.CharField(max_length=30)
	chequecount=models.IntegerField()
	lastno=models.CharField(max_length=30)
	issuedate=models.DateField()