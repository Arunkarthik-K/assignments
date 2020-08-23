from rest_framework import serializers
from .models import User, Group, ExpenseModel, CATEGORIES, STATUS
import datetime

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseModel
        fields ="__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CreateSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data['Categories'] == "TRA":
            if data['Amount'] > 7500:
                raise serializers.ValidationError("Amount should be less or equal to 7500 for Travel") 
                if data['Trans_Date'] > data['Date_of_Sub']:
                    raise serializers.ValidationError("Trans_Date should not be future") 
                elif data['Trans_Date'] < (data['Date_of_Sub'] - datetime.timedelta(days=90)):   
                    raise serializers.ValidationError("Trans_Date should not be older than 3 months")    
            elif data['Trans_Date'] > data['Date_of_Sub']:
                    raise serializers.ValidationError("Trans_Date should not be future")   
            elif data['Trans_Date'] < (data['Date_of_Sub'] - datetime.timedelta(days=90)):   
                raise serializers.ValidationError("Trans_Date should not be older than 3 months")      
        elif data['Categories'] == "MISC":
            if data['Amount'] > 1500:
                raise serializers.ValidationError("Amount should be less or equal to 1500 for Misc")
                if data['Trans_Date'] > data['Date_of_Sub']:
                    raise serializers.ValidationError("Trans_Date should not be future") 
                elif data['Trans_Date'] < (data['Date_of_Sub'] - datetime.timedelta(days=90)):   
                    raise serializers.ValidationError("Trans_Date should not be older than 3 months")    
            elif data['Trans_Date'] > data['Date_of_Sub']:
                    raise serializers.ValidationError("Trans_Date should not be future")   
            elif data['Trans_Date'] < (data['Date_of_Sub'] - datetime.timedelta(days=90)):   
                raise serializers.ValidationError("Trans_Date should not be older than 3 months") 
        elif data['Trans_Date'] > data['Date_of_Sub']:
                    raise serializers.ValidationError("Trans_Date should not be future")   
        elif data['Trans_Date'] < (data['Date_of_Sub'] - datetime.timedelta(days=90)): 
            raise serializers.ValidationError("Trans_Date should not be older than 3 months")            

        return data

    class Meta:
        model = ExpenseModel
        fields ="__all__"       
               
class UpdateSerializer(serializers.ModelSerializer):
    Status = serializers.ChoiceField(choices=STATUS,read_only=True)

    def validate(self, data):
        if data['Categories'] == "TRA":
            if data['Amount'] > 7500:
                raise serializers.ValidationError("Amount should be less or equal to 7500 for Travel") 
                if data['Trans_Date'] > data['Date_of_Sub']:
                    raise serializers.ValidationError("Trans_Date should not be future") 
                elif data['Trans_Date'] < (data['Date_of_Sub'] - datetime.timedelta(days=90)):   
                    raise serializers.ValidationError("Trans_Date should not be older than 3 months")    
            elif data['Trans_Date'] > data['Date_of_Sub']:
                    raise serializers.ValidationError("Trans_Date should not be future")   
            elif data['Trans_Date'] < (data['Date_of_Sub'] - datetime.timedelta(days=90)):   
                raise serializers.ValidationError("Trans_Date should not be older than 3 months")      
        elif data['Categories'] == "MISC":
            if data['Amount'] > 1500:
                raise serializers.ValidationError("Amount should be less or equal to 1500 for Misc")
                if data['Trans_Date'] > data['Date_of_Sub']:
                    raise serializers.ValidationError("Trans_Date should not be future") 
                elif data['Trans_Date'] < (data['Date_of_Sub'] - datetime.timedelta(days=90)):   
                    raise serializers.ValidationError("Trans_Date should not be older than 3 months")    
            elif data['Trans_Date'] > data['Date_of_Sub']:
                    raise serializers.ValidationError("Trans_Date should not be future")   
            elif data['Trans_Date'] < (data['Date_of_Sub'] - datetime.timedelta(days=90)):   
                raise serializers.ValidationError("Trans_Date should not be older than 3 months") 
        elif data['Trans_Date'] > data['Date_of_Sub']:
                    raise serializers.ValidationError("Trans_Date should not be future")   
        elif data['Trans_Date'] < (data['Date_of_Sub'] - datetime.timedelta(days=90)): 
            raise serializers.ValidationError("Trans_Date should not be older than 3 months")            

        return data

    class Meta:
        model = ExpenseModel
        fields ="__all__"          

class Update2Serializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseModel
        fields ="__all__"  
        read_only_fields = ('Title', 'Description', 'Amount', 'Categories', 'Trans_Date', 'Image', 'Emp', 'Date_of_Sub',)                      