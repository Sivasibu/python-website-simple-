from rest_framework import serializers
from. models import Students

class StudentSerializer(serializers.ModelSerializer):
    updated_by =serializers.CharField(source='created_by.username',read_only=True)

    class Meta:
        model = Students
        fields = ("__all__")
        
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.address = validated_data.get('address',instance.address)
        instance.roll_number = validated_data.get('roll_number',instance.roll_number)
        instance.mobile = validated_data.get('mobile',instance.mobile)
        instance.updated_by = self.context['request'].user
        instance.save()
        return instance
