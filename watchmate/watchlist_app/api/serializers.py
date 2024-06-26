from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        exclude = ['watchlist']
        # fields = "__all__"

# Model Serializers --------------------------------
class WatchListSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WatchList
        # Hepsini dahil eder.
        fields = "__all__"

        # Bu alanları dahil etmez
        # exclude = ['active', 'description']


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="stream_details")

    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'


################################################################

# def name_length(name):
#     if len(name) < 2:
#         raise serializers.ValidationError('Name is too short')

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and Description should not be different')
#         else:
#             return data
        

    # Name'i direk kontrol eder        
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short')
    #     else:
    #         return value