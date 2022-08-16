from rest_framework import serializers

from .models import User, Association , Memberassociation , Organization


# start Association

class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Association
        fields=('id','user', 'nameassociation', 'emailassociation', 'phoneassociation','type',
                'addressassociation', 'cityassociation', 'Objectivesassociation','informationsassociation','get_logoassociation', 'image')

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Memberassociation
        fields=('id', 'member_association', 'association','type_member_association')

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Organization
        fields=('id','president_of_organisation', 'nameorganisation', 'emailorganisation', 'phoneorganisation','type',
                'addressorganisation', 'cityorganisation', 'Objectivesorganisation','informationsorganisation',
                'get_image', 'get_logoorganisation', 'image', 'logoorganisation')

# end Association
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'is_admin_assoc','is_member_assoc','is_admin_orga']

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Association
        fields=['pk','nameassociation', 'phoneassociation', 'user']

class AssociationAdminSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2','birth_date' ,'address','city','cin','phone_number', 'first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        username=self.validated_data['username']
        email=self.validated_data['email']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        birth_date = self.validated_data['birth_date']
        address= self.validated_data['address']
        city = self.validated_data['city']
        cin = self.validated_data['cin']
        phone_number = self.validated_data['phone_number']

        if password != password2:
            raise serializers.ValidationError({"error": "password do not match"})
        user = User.objects.create(username=username,email=email ,
                            birth_date=birth_date ,address=address , city=city,
                            cin=cin , phone_number=phone_number, first_name=first_name,
                            last_name=last_name ,is_admin_assoc = True , is_active=True)
        user.set_password(password)
        user.save()
        return user

class AssociationMemberSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2','birth_date' ,'address','city','cin','phone_number', 'first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        username=self.validated_data['username']
        email=self.validated_data['email']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        birth_date = self.validated_data['birth_date']
        address= self.validated_data['address']
        city = self.validated_data['city']
        cin = self.validated_data['cin']
        phone_number = self.validated_data['phone_number']

        if password != password2:
            raise serializers.ValidationError({"error": "password do not match"})
        user = User.objects.create(username=username,email=email ,
                            birth_date=birth_date ,address=address , city=city,
                            cin=cin , phone_number=phone_number, first_name=first_name,
                            last_name=last_name ,is_member_assoc = True , is_active=True)
        user.set_password(password)
        user.save()
        return user

class OrganizationAdminSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2','birth_date' ,'address','city','cin','phone_number', 'first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        username=self.validated_data['username']
        email=self.validated_data['email']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        birth_date = self.validated_data['birth_date']
        address= self.validated_data['address']
        city = self.validated_data['city']
        cin = self.validated_data['cin']
        phone_number = self.validated_data['phone_number']

        if password != password2:
            raise serializers.ValidationError({"error": "password do not match"})
        user = User.objects.create(username=username,email=email ,
                            birth_date=birth_date ,address=address , city=city,
                            cin=cin , phone_number=phone_number, first_name=first_name,
                            last_name=last_name ,is_admin_orga = True , is_active=True)
        user.set_password(password)
        user.save()
        return user

