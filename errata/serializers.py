from .models import Errata, Book

from rest_framework import serializers


class ErrataSerializer(serializers.ModelSerializer):
    resolution_date = serializers.DateField(read_only=True)

    class Meta:
        model = Errata
        fields = ('id',
                  'created',
                  'modified',
                  'openstax_book',
                  'book',
                  'status',
                  'resolution',
                  'reviewed_date',
                  'corrected_date',
                  'archived',
                  'is_assessment_errata',
                  'location',
                  'detail',
                  'short_detail',
                  'resolution_date',
                  'resolution_notes',
                  'error_type',
                  'error_type_other',
                  'resource',
                  'resource_other',
                  'submitted_by_account_id',
                  'file_1',
                  'file_2')


class BookSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(BookSerializer, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].read_only = True

    class Meta:
        model = Book
        fields = '__all__'