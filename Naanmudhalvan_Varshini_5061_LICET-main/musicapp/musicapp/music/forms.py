from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'genre', 'audio_file', 'cover_image']

    def clean_audio_file(self):
        audio_file = self.cleaned_data['audio_file']
        # Add validation logic if needed (e.g., file size, file type)
        return audio_file
